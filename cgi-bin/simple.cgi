#! /bin/bash

# This is a little CGI program
###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The desired MIME type for the response.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.
# HTTP_USER_AGENT:   Information about the requesting client.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request.
# REQUEST_URI:       The URI of the request.
# SERVER_PROTOCOL:   Currently âHTTP/1.1â
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address.
# SERVER_PORT:       The port of the server.


echo "Content-type: text/html"
echo ""

echo "Enter in a Query String in order to navigate web pages"
echo ""
echo "www.csun.edu/~agn53527/cgi-bin/simple.cgi?csun to go to the csun.edu homepage"
echo ""
echo "Here are the system's environment variables..."
echo ""
echo "<pre> $(env) </pre>"
if [ "$QUERY_STRING" == "index.html" ];  then
   echo "Taking you to index.html..."
   /usr/bin/curl -s "www.csun.edu/~agn53527/"
elif [ "${QUERY_STRING}" == "csun" ] ; then
   echo "Taking you to www.csun.edu"
   /usr/bin/curl -s "www.csun.edu"
else
   echo "That Query String doesn't work, try csun or index.html"
fi
