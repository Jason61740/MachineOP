#!/bin/bash
echo "🔍 TESTING LAKEFS SETUP"
echo "======================"

echo "1. Container status:"
/Applications/Docker.app/Contents/Resources/bin/docker ps | grep lakefs

echo "2. Web interface:"
curl -s http://localhost:8000 | head -1

echo "3. lakectl version:"
lakectl --version

echo "4. Ready to version data!"
echo "Next: Open http://localhost:8000 to complete setup"
