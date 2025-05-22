filename="hello.txt"

# Check if file exists
if [ -f "$filename" ]; then
    echo "$filename exists. Deleting and recreating it..."
    rm "$filename"
else
    echo "$filename does not exist. Creating it..."
fi

# Create the file
echo This file was created on: `date` > "$filename"

echo '$filename created successfully with content:'
cat "$filename"
