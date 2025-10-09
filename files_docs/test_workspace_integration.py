#!/usr/bin/env python3
"""
Project Workspaces Integration Test
Verifies that the deployment integrates properly with existing systems
"""

import os
import json
from pathlib import Path
from datetime import datetime

class IntegrationTester:
    def __init__(self):
        self.home = Path.home()
        self.knowledge_map_dir = self.home / "Documents" / "_AUTOMATION" / "knowledge_map"
        self.project_workspaces = self.knowledge_map_dir / "Project_Workspaces"
        self.test_results = []
        
    def test_directory_structure(self):
        """Verify that all expected directories exist"""
        print("🔍 Testing directory structure...")
        
        expected_dirs = [
            self.project_workspaces / "ClaudeOfficeSpace",
            self.project_workspaces / "ClaudeOfficeSpace" / "Technical_Designs",
            self.project_workspaces / "ClaudeOfficeSpace" / "Project_Artifacts",
            self.project_workspaces / "ClaudeOfficeSpace" / "Knowledge_Management",
            self.project_workspaces / "ClaudeOfficeSpace" / "Active_Development",
        ]
        
        all_exist = True
        for dir_path in expected_dirs:
            if dir_path.exists():
                print(f"   ✅ {dir_path.relative_to(self.knowledge_map_dir)}")
            else:
                print(f"   ❌ Missing: {dir_path.relative_to(self.knowledge_map_dir)}")
                all_exist = False
        
        self.test_results.append(("Directory Structure", all_exist))
        return all_exist
    
    def test_knowledge_map_integration(self):
        """Test if knowledge map generator recognizes new workspaces"""
        print("\n🗺️ Testing knowledge map integration...")
        
        # Check if config.py includes Project_Workspaces
        config_path = self.knowledge_map_dir / "config.py"
        if config_path.exists():
            config_content = config_path.read_text()
            has_workspaces = "Project_Workspaces" in config_content
            has_claude = "ClaudeOfficeSpace" in config_content
            
            if has_workspaces and has_claude:
                print("   ✅ Knowledge map config includes Project_Workspaces")
                self.test_results.append(("Knowledge Map Config", True))
                return True
            else:
                print("   ❌ Knowledge map config missing workspace references")
                self.test_results.append(("Knowledge Map Config", False))
                return False
        else:
            print("   ❌ Knowledge map config not found")
            self.test_results.append(("Knowledge Map Config", False))
            return False
    
    def test_automation_scripts(self):
        """Test if automation scripts are properly created"""
        print("\n⚙️ Testing automation scripts...")
        
        automation_script = self.project_workspaces / "workspace_automation.py"
        if automation_script.exists():
            # Check if it's executable
            is_executable = os.access(automation_script, os.X_OK)
            if is_executable:
                print("   ✅ Automation script is executable")
            else:
                print("   ⚠️ Automation script exists but not executable")
            
            # Check if it has proper content
            content = automation_script.read_text()
            has_class = "class WorkspaceAutomation" in content
            has_methods = all(method in content for method in 
                            ["sort_incoming_files", "cleanup_old_files", "generate_workspace_report"])
            
            if has_class and has_methods:
                print("   ✅ Automation script has required methods")
                self.test_results.append(("Automation Scripts", True))
                return True
            else:
                print("   ❌ Automation script missing required methods")
                self.test_results.append(("Automation Scripts", False))
                return False
        else:
            print("   ❌ Automation script not found")
            self.test_results.append(("Automation Scripts", False))
            return False
    
    def test_documentation(self):
        """Test if documentation files are created"""
        print("\n📚 Testing documentation...")
        
        docs = [
            self.project_workspaces / "README.md",
            self.project_workspaces / "ClaudeOfficeSpace" / "README.md"
        ]
        
        all_docs_exist = True
        for doc_path in docs:
            if doc_path.exists():
                print(f"   ✅ {doc_path.name} exists")
            else:
                print(f"   ❌ {doc_path.name} missing")
                all_docs_exist = False
        
        self.test_results.append(("Documentation", all_docs_exist))
        return all_docs_exist
    
    def test_sample_file_placement(self):
        """Test file placement in appropriate categories"""
        print("\n📁 Testing sample file placement...")
        
        # Create a test file and see if automation would categorize it correctly
        test_scenarios = [
            ("test_architecture_design.md", "Technical_Designs"),
            ("project_requirements_v1.pdf", "Project_Artifacts"),
            ("best_practices_guide.md", "Knowledge_Management"),
            ("prototype_demo.py", "Active_Development")
        ]
        
        categorization_works = True
        for filename, expected_category in test_scenarios:
            # Check if the category directory exists
            category_path = self.project_workspaces / "ClaudeOfficeSpace" / expected_category
            if category_path.exists():
                print(f"   ✅ {expected_category} ready for {filename}")
            else:
                print(f"   ❌ {expected_category} not available")
                categorization_works = False
        
        self.test_results.append(("File Categorization", categorization_works))
        return categorization_works
    
    def generate_test_report(self):
        """Generate a test results report"""
        print("\n" + "=" * 50)
        print("📊 INTEGRATION TEST RESULTS")
        print("=" * 50)
        
        passed = sum(1 for _, result in self.test_results if result)
        total = len(self.test_results)
        
        for test_name, result in self.test_results:
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{test_name:.<30} {status}")
        
        print("=" * 50)
        print(f"Overall: {passed}/{total} tests passed")
        
        if passed == total:
            print("\n🎉 All integration tests passed!")
            print("Your Project Workspaces are fully integrated and ready to use.")
        else:
            print(f"\n⚠️ {total - passed} test(s) failed.")
            print("Please review the deployment and fix any issues.")
        
        # Save report
        report_path = self.knowledge_map_dir / f"integration_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_path, 'w') as f:
            f.write(f"Integration Test Report\n")
            f.write(f"Generated: {datetime.now()}\n\n")
            for test_name, result in self.test_results:
                f.write(f"{test_name}: {'PASS' if result else 'FAIL'}\n")
            f.write(f"\nOverall: {passed}/{total} tests passed\n")
        
        print(f"\n📄 Report saved: {report_path.name}")
        
        return passed == total
    
    def run_tests(self):
        """Execute all integration tests"""
        print("🧪 Running Project Workspaces Integration Tests")
        print("=" * 50)
        
        # Run all tests
        self.test_directory_structure()
        self.test_knowledge_map_integration()
        self.test_automation_scripts()
        self.test_documentation()
        self.test_sample_file_placement()
        
        # Generate report
        all_passed = self.generate_test_report()
        
        return all_passed

if __name__ == "__main__":
    tester = IntegrationTester()
    success = tester.run_tests()
    
    if success:
        print("\n✅ Integration successful! Your workspace is ready.")
        print("\n🚀 Quick Start Commands:")
        print("   cd ~/Documents/_AUTOMATION/knowledge_map/Project_Workspaces/ClaudeOfficeSpace")
        print("   ls -la")
    else:
        print("\n⚠️ Some integration issues detected. Please review and fix.")
