#!/usr/bin/env python3
"""
Generic Downloads Folder Organizer
Organizes any user's Downloads folder into topic-based categories
"""

import os
import shutil
import platform
from pathlib import Path
from datetime import datetime

class DownloadsOrganizer:
    def __init__(self):
        self.downloads_path = self.get_downloads_path()
        self.organized_path = self.downloads_path / "_ORGANIZED"
        self.projects_path = self.organized_path / "Projects_By_Topic"
        
        # Generic categories - customize as needed
        self.categories = {
            "Documents/Work": [".pdf", ".docx", ".doc", ".txt", ".rtf"],
            "Documents/Personal": [],  # Manual sorting
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
            "Videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
            "Audio": [".mp3", ".wav", ".flac", ".aac"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Software": [".dmg", ".exe", ".msi", ".pkg", ".deb"],
            "Spreadsheets": [".xlsx", ".xls", ".csv"],
            "Presentations": [".pptx", ".ppt", ".key"],
            "Code": [".py", ".js", ".html", ".css", ".json"],
            "Temporary": []  # For manual review
        }
        
        self.moved_files = []
        self.failed_files = []
        
    def get_downloads_path(self):
        """Auto-detect Downloads folder for current user"""
        system = platform.system()
        home = Path.home()
        
        if system == "Darwin":  # macOS
            return home / "Downloads"
        elif system == "Windows":
            return home / "Downloads"
        else:  # Linux
            return home / "Downloads"
    
    def count_files(self, directory):
        """Count total files in directory and subdirectories"""
        try:
            return sum([len(files) for r, d, files in os.walk(directory)])
        except:
            return 0
    
    def create_folder_structure(self):
        """Create organized folder structure"""
        print(f"📁 Creating folder structure in {self.organized_path}")
        
        for category in self.categories.keys():
            folder_path = self.organized_path / category
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"   Created: {category}")
    
    def categorize_file(self, file_path):
        """Determine which category a file belongs to"""
        file_ext = file_path.suffix.lower()
        
        for category, extensions in self.categories.items():
            if file_ext in extensions:
                return category
        
        return "Temporary"  # Uncategorized files for manual review
    
    def run_pre_audit(self):
        """Count files before organization"""
        self.original_count = self.count_files(self.downloads_path)
        print(f"🔍 Pre-audit: Found {self.original_count} total files")
        
        # Count loose files in Downloads root
        loose_files = [f for f in self.downloads_path.iterdir() 
                      if f.is_file() and not f.name.startswith('.')]
        print(f"📄 Files to organize: {len(loose_files)}")
        return loose_files
    
    def test_move(self, files):
        """Test moving 3 files first"""
        test_files = files[:3] if len(files) >= 3 else files
        print(f"🧪 Testing with {len(test_files)} files...")
        
        for file_path in test_files:
            category = self.categorize_file(file_path)
            dest_folder = self.organized_path / category
            dest_path = dest_folder / file_path.name
            
            try:
                shutil.move(str(file_path), str(dest_path))
                self.moved_files.append(file_path.name)
                print(f"   ✅ Test moved: {file_path.name} → {category}")
            except Exception as e:
                self.failed_files.append((file_path.name, str(e)))
                print(f"   ❌ Test failed: {file_path.name} - {e}")
        
        if self.failed_files:
            print("⚠️  Test failures detected. Check permissions/disk space.")
            return False
        return True
    
    def organize_files(self, files):
        """Organize remaining files"""
        remaining_files = files[3:] if len(files) >= 3 else []
        
        print(f"📦 Organizing {len(remaining_files)} remaining files...")
        
        for file_path in remaining_files:
            category = self.categorize_file(file_path)
            dest_folder = self.organized_path / category
            dest_path = dest_folder / file_path.name
            
            try:
                shutil.move(str(file_path), str(dest_path))
                self.moved_files.append(file_path.name)
                print(f"   ✅ Moved: {file_path.name} → {category}")
            except Exception as e:
                self.failed_files.append((file_path.name, str(e)))
                print(f"   ❌ Failed: {file_path.name} - {e}")
    
    def run_post_audit(self):
        """Verify organization completed successfully"""
        final_count = self.count_files(self.downloads_path)
        moved_count = len(self.moved_files)
        failed_count = len(self.failed_files)
        
        print(f"\n📊 Post-audit Results:")
        print(f"   Original files: {self.original_count}")
        print(f"   Final files: {final_count}")
        print(f"   Successfully moved: {moved_count}")
        print(f"   Failed to move: {failed_count}")
        
        # Check integrity
        integrity_check = (self.original_count == final_count)
        print(f"   Integrity check: {'✅ PASSED' if integrity_check else '❌ FAILED'}")
        
        if self.failed_files:
            print(f"\n⚠️  Failed files:")
            for file_name, error in self.failed_files:
                print(f"   • {file_name}: {error}")
    
    def generate_report(self):
        """Generate organization report"""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_path = self.downloads_path / f"organization_report_{timestamp}.txt"
        
        with open(report_path, 'w') as f:
            f.write(f"Downloads Organization Report - {timestamp}\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Downloads path: {self.downloads_path}\n")
            f.write(f"Total files processed: {len(self.moved_files) + len(self.failed_files)}\n")
            f.write(f"Successfully organized: {len(self.moved_files)}\n")
            f.write(f"Failed to organize: {len(self.failed_files)}\n\n")
            
            if self.moved_files:
                f.write("Successfully moved files:\n")
                for file_name in self.moved_files:
                    f.write(f"  • {file_name}\n")
                f.write("\n")
            
            if self.failed_files:
                f.write("Failed files:\n")
                for file_name, error in self.failed_files:
                    f.write(f"  • {file_name}: {error}\n")
        
        print(f"📄 Report saved: {report_path}")
    
    def run(self):
        """Main execution flow"""
        print("🗂️  Downloads Folder Organizer")
        print("=" * 40)
        print(f"Working on: {self.downloads_path}")
        
        # Create folder structure
        self.create_folder_structure()
        
        # Pre-audit
        files_to_organize = self.run_pre_audit()
        
        if not files_to_organize:
            print("✨ No files to organize!")
            return
        
        # Test with small batch
        if not self.test_move(files_to_organize):
            print("❌ Testing failed. Aborting.")
            return
        
        # Organize remaining files
        self.organize_files(files_to_organize)
        
        # Post-audit
        self.run_post_audit()
        
        # Generate report
        self.generate_report()
        
        print(f"\n🎉 Organization complete!")
        print(f"📁 Organized files are in: {self.organized_path}")

if __name__ == "__main__":
    organizer = DownloadsOrganizer()
    organizer.run()
