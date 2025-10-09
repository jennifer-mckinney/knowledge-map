#!/usr/bin/env python3
"""
Dynamic Knowledge Map Generator
Scans file system and generates JSON data for visualization
"""

import json
from pathlib import Path
from datetime import datetime

def scan_file_system():
    """Scan and generate current file system data"""
    
    nodes = []
    links = []
    node_map = {}
    node_id = 0
    
    # Define locations to scan
    locations = [
        ("docs", Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Documents", "location"),
        ("downloads", Path.home() / "Downloads", "location")
    ]
    
    # Scan each location
    for loc_id, loc_path, loc_type in locations:
        if not loc_path.exists():
            continue

        # BUG FIX #5: Add error handling for permission denied and other scanning errors
        # Without this, the script crashes when encountering protected directories
        try:
            # Count total files in location
            total_files = sum(1 for f in loc_path.rglob('*') if f.is_file() and not f.name.startswith('.'))
        except PermissionError:
            print(f"⚠️  Permission denied accessing {loc_path}")
            total_files = 0
        except Exception as e:
            print(f"⚠️  Error scanning {loc_path}: {e}")
            total_files = 0
        
        # Add location node
        node_map[str(loc_path)] = loc_id
        nodes.append({
            "id": loc_id,
            "name": loc_path.name,
            "category": loc_type,
            "files": total_files,
            "size": min(40, max(10, total_files // 20)),
            "path": str(loc_path)
        })
        
        # Scan subdirectories
        for subdir in loc_path.iterdir():
            if subdir.is_dir() and not subdir.name.startswith('.'):
                # BUG FIX #5: Error handling for subdirectory scanning
                try:
                    file_count = sum(1 for f in subdir.rglob('*') if f.is_file() and not f.name.startswith('.'))
                except PermissionError:
                    print(f"⚠️  Permission denied accessing {subdir}")
                    continue  # Skip this subdirectory
                except Exception as e:
                    print(f"⚠️  Error scanning {subdir}: {e}")
                    continue  # Skip this subdirectory
                
                if file_count > 0:
                    sub_id = f"node_{node_id}"
                    node_id += 1
                    
                    # Determine category
                    category = "general"
                    if "_AUTOMATION" in subdir.name:
                        category = "system"
                    elif "Career" in subdir.name or "Professional" in subdir.name:
                        category = "professional"
                    elif "Education" in subdir.name or "Course" in subdir.name:
                        category = "education"
                    elif "Research" in subdir.name or "AI" in subdir.name:
                        category = "research"
                    elif "Technical" in subdir.name or "Development" in subdir.name:
                        category = "technical"
                    elif "_ORGANIZED" in subdir.name:
                        category = "system"
                    
                    nodes.append({
                        "id": sub_id,
                        "name": subdir.name,
                        "category": category,
                        "files": file_count,
                        "size": min(30, max(5, file_count // 5)),
                        "path": str(subdir)
                    })
                    
                    # Link to parent
                    links.append({
                        "source": loc_id,
                        "target": sub_id,
                        "strength": 0.8
                    })
                    
                    # Scan one more level deep for important folders
                    if subdir.name in ["_AUTOMATION", "_ORGANIZED", "Projects_By_Topic"]:
                        for subsubdir in subdir.iterdir():
                            if subsubdir.is_dir() and not subsubdir.name.startswith('.'):
                                # BUG FIX #5: Error handling for deep subdirectory scanning
                                try:
                                    subfile_count = sum(1 for f in subsubdir.rglob('*') if f.is_file())
                                except PermissionError:
                                    print(f"⚠️  Permission denied accessing {subsubdir}")
                                    continue  # Skip this deep subdirectory
                                except Exception as e:
                                    print(f"⚠️  Error scanning {subsubdir}: {e}")
                                    continue  # Skip this deep subdirectory
                                
                                if subfile_count > 0:
                                    subsub_id = f"node_{node_id}"
                                    node_id += 1
                                    
                                    nodes.append({
                                        "id": subsub_id,
                                        "name": subsubdir.name,
                                        "category": category,
                                        "files": subfile_count,
                                        "size": min(20, max(5, subfile_count // 3)),
                                        "path": str(subsubdir)
                                    })
                                    
                                    links.append({
                                        "source": sub_id,
                                        "target": subsub_id,
                                        "strength": 0.7
                                    })
    
    # Add semantic relationships
    for i, n1 in enumerate(nodes):
        for n2 in nodes[i+1:]:
            # Check for related topics
            keywords = ['ai', 'research', 'career', 'oxford', 'technical', 'project']
            if any(k in n1['name'].lower() and k in n2['name'].lower() for k in keywords):
                links.append({
                    "source": n1['id'],
                    "target": n2['id'],
                    "strength": 0.3
                })
    
    return {
        "nodes": nodes,
        "links": links,
        "generated": datetime.now().isoformat(),
        "total_files": sum(n['files'] for n in nodes)
    }

def save_data(data, output_path):
    """Save data to JSON file"""
    # BUG FIX #7: Add error handling for file write failures
    # This prevents silent failures when disk is full or permissions are wrong
    try:
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✓ Saved {len(data['nodes'])} nodes, {data['total_files']} total files")
    except PermissionError:
        print(f"❌ Permission denied writing to {output_path}")
        print(f"   Check file permissions and try again")
        raise  # Re-raise to let caller know the save failed
    except OSError as e:
        print(f"❌ Disk error writing to {output_path}: {e}")
        print(f"   Check available disk space and file system health")
        raise  # Re-raise to let caller know the save failed
    except Exception as e:
        print(f"❌ Unexpected error saving data: {e}")
        raise  # Re-raise to let caller know the save failed

if __name__ == "__main__":
    # Generate data
    data = scan_file_system()
    
    # Save to iCloud Documents
    output = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Documents/knowledge_map_data.json"
    save_data(data, output)
    
    print(f"Data saved to: {output}")
    print("Open knowledge_map_dynamic.html to view")
