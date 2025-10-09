#!/bin/bash

# Project Workspaces Deployment Wrapper
# Simplifies deployment execution and provides integration options

echo "🚀 Project Workspaces Deployment System"
echo "========================================"
echo ""

# Set paths
AUTOMATION_DIR="/Users/jennifermckinney/Documents/_AUTOMATION"
KNOWLEDGE_MAP_DIR="$AUTOMATION_DIR/knowledge_map"
DEPLOY_SCRIPT="/mnt/user-data/outputs/deploy_project_workspaces.py"

# Check if knowledge_map directory exists
if [ ! -d "$KNOWLEDGE_MAP_DIR" ]; then
    echo "❌ Knowledge map directory not found at: $KNOWLEDGE_MAP_DIR"
    echo "   Please ensure the knowledge map system is installed first."
    exit 1
fi

echo "📍 Target directory: $KNOWLEDGE_MAP_DIR/Project_Workspaces"
echo ""
echo "This deployment will:"
echo "  • Create Project_Workspaces structure"
echo "  • Set up ClaudeOfficeSpace with 4 main categories"
echo "  • Create placeholder workspaces for future projects"
echo "  • Update knowledge map configuration"
echo "  • Integrate with existing automation system"
echo ""

read -p "Do you want to proceed with deployment? (y/N): " response

if [[ ! "$response" =~ ^[Yy]$ ]]; then
    echo "Deployment cancelled."
    exit 0
fi

echo ""
echo "🔄 Starting deployment..."
echo ""

# Copy deployment script to knowledge_map directory for execution
cp "$DEPLOY_SCRIPT" "$KNOWLEDGE_MAP_DIR/deploy_project_workspaces.py"
chmod +x "$KNOWLEDGE_MAP_DIR/deploy_project_workspaces.py"

# Execute the deployment
cd "$KNOWLEDGE_MAP_DIR"
python3 deploy_project_workspaces.py

# Check if deployment was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Deployment completed successfully!"
    echo ""
    echo "📁 Project Workspaces Structure:"
    echo ""
    # Show the created structure
    if [ -d "$KNOWLEDGE_MAP_DIR/Project_Workspaces" ]; then
        tree -L 3 "$KNOWLEDGE_MAP_DIR/Project_Workspaces" 2>/dev/null || \
        find "$KNOWLEDGE_MAP_DIR/Project_Workspaces" -type d -maxdepth 3 | sort | sed 's|'"$KNOWLEDGE_MAP_DIR/Project_Workspaces"'|Project_Workspaces|' | head -20
    fi
    echo ""
    echo "🎯 Next Steps:"
    echo "   1. cd $KNOWLEDGE_MAP_DIR/Project_Workspaces/ClaudeOfficeSpace"
    echo "   2. Start adding your technical artifacts"
    echo "   3. Run: $KNOWLEDGE_MAP_DIR/generate_map.sh"
    echo "   4. Access via Control Center for management"
    
    # Offer to update control center
    echo ""
    read -p "Would you like to update the Control Center with Project Workspaces access? (y/N): " update_cc
    
    if [[ "$update_cc" =~ ^[Yy]$ ]]; then
        echo "🔧 Updating Control Center..."
        # Create integration patch for control center
        cat > "$KNOWLEDGE_MAP_DIR/update_control_center.sh" << 'EOF'
#!/bin/bash

# Add Project Workspaces option to Control Center

CONTROL_CENTER="/Users/jennifermckinney/Documents/_AUTOMATION/control_center.sh"

if [ -f "$CONTROL_CENTER" ]; then
    # Check if already integrated
    if grep -q "Project Workspaces" "$CONTROL_CENTER"; then
        echo "✅ Control Center already has Project Workspaces integration"
    else
        # Add to the knowledge map case statement
        sed -i.bak '/km_choice in/a\
4)\
echo "📁 Opening Project Workspaces..."\
cd "$AUTOMATION_DIR/knowledge_map/Project_Workspaces"\
ls -la\
echo ""\
echo "Available Workspaces:"\
for dir in */; do echo "  • $dir"; done\
echo ""\
read -p "Enter workspace name to open (or press Enter to cancel): " workspace\
if [ -n "$workspace" ] && [ -d "$workspace" ]; then\
    cd "$workspace"\
    echo "📍 Now in: $(pwd)"\
    ls -la\
else\
    echo "Cancelled"\
fi\
;;' "$CONTROL_CENTER"
        
        echo "✅ Control Center updated with Project Workspaces access"
    fi
else
    echo "❌ Control Center not found at expected location"
fi
EOF
        
        chmod +x "$KNOWLEDGE_MAP_DIR/update_control_center.sh"
        "$KNOWLEDGE_MAP_DIR/update_control_center.sh"
    fi
    
else
    echo ""
    echo "❌ Deployment encountered errors."
    echo "Please check the deployment report in:"
    echo "$KNOWLEDGE_MAP_DIR/deployment_report_*.md"
fi

echo ""
echo "📚 Documentation available at:"
echo "   • $KNOWLEDGE_MAP_DIR/Project_Workspaces/README.md"
echo "   • $KNOWLEDGE_MAP_DIR/Project_Workspaces/ClaudeOfficeSpace/README.md"
