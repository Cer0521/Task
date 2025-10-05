use('inventory_db');

db.getCollection('filtered_inventory').insertMany([
  {
    "Item ID": 2001,
    "Item Name": "SSD Drive",
    "Year 2024": 80.0,
    "Year 2025": 95.0,
    "Cost Increase": 15.0,
    "% Increase": 18.75
  },
  {
    "Item ID": 2002,
    "Item Name": "Graphics Card",
    "Year 2024": 350.0,
    "Year 2025": 400.0,
    "Cost Increase": 50.0,
    "% Increase": 14.29
  },
  {
    "Item ID": 2003,
    "Item Name": "Mechanical Keyboard",
    "Year 2024": 60.0,
    "Year 2025": 70.0,
    "Cost Increase": 10.0,
    "% Increase": 16.67
  },
  {
    "Item ID": 2005,
    "Item Name": "DDR4 RAM 16GB",
    "Year 2024": 75.0,
    "Year 2025": 90.0,
    "Cost Increase": 15.0,
    "% Increase": 20.0
  }
]);

// Optional: View all documents in the collection
db.getCollection('filtered_inventory').find({});