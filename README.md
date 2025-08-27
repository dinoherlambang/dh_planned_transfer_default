# Planned Transfer Option

## What it does

Adds a checkbox to operation types to set default transfer mode to be **Planned Transfer** option.

## Why you need this

**Problem**: Odoo defaults to "Immediate Transfer" which hides the Demand column. OCA serial number import modules (like `stock_picking_import_serial_number`) need the Demand column to work properly.

**Solution**: Check "Default to Planned Transfer" on operation types that need serial number imports. If you use OCA stock picking serial number import modules it will make much easier to use.


## Installation

1. Install module from Apps menu
2. Go to **Inventory → Configuration → Operation Types**  
3. Edit an operation type (e.g., "Receipts")
4. Check **"Default to Planned Transfer"**
5. Save

## Usage

- **Planned Transfer**: Shows Demand + Done columns, required for serial number imports
- **Immediate Transfer**: Shows only Done column, faster for simple operations

## Recommended Setup

- ✅ **Receipts**: Enable (for importing serial numbers)
- ❌ **Delivery Orders**: Keep disabled (for speed)

## Using with OCA Serial Number Import Module

If you have the OCA `stock_picking_import_serial_number` module installed:

1. **Create a planned transfer** (using configured operation type)
2. **Add products** with tracking = "By Unique Serial Number"
3. **Set quantities** in the Demand column (e.g., quantity 3 for 3 serials)
4. **Prepare your import file** (Excel/CSV):
   ```
   Reference    Serial Number
   LAPTOP001    SN100
   LAPTOP001    SN101
   LAPTOP001    SN102
   ```
5. **Click "Import S/N"** button in the transfer
6. **Upload your file** and import
7. **Validate the transfer** - serial numbers are now assigned!

**Note**: Without this module, you'd have to manually create each transfer in planned mode every time.

That's it! Now your serial number imports will work properly.

## Author

Created by **Dino Herlambang**

## License

This module is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

You are free to:
- Use this software for any purpose
- Study and modify the source code
- Distribute copies
- Distribute modified versions

Under the following conditions:
- Any derivative work must also be licensed under GPL-3.0
- You must include the original copyright notice
- You must include the license text

For more details, see the [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.html).
