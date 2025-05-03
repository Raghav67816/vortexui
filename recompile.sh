cd /mnt/Sector16/fui-lib
source env/bin/active

echo "Running setup.py"

python3 setup.py bdist_wheel
pip3 uninstall vortexui


echo "Installing re-compiled version"
cd /mnt/Sector16/fui-lib/dist
pip3 install vortexui-0.0.1-py3-none-any.whl