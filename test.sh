# configure python virtual environment and install dependencies
install_dir=/opt/flask-app
sudo su - pythonadm << EOF
cd ${install_dir}
source venv/bin/activate
pytest --cov-config=.coveragerc --cov-report html:cov_html --cov=. testing
mv cov_html/index.html flask_app/templates/coveragereport.html
rm -r cov_html
EOF
