---
title: serial_ports
hide_title: false
hide_table_of_contents: false
keywords:
  - serial_ports
  - serial_console
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serial_ports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.serial_console.serial_ports</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SerialPorts_Get` | `SELECT` | `parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, serialPort, subscriptionId` | Gets the configured settings for a serial port |
| `SerialPorts_List` | `SELECT` | `parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, subscriptionId` | Lists all of the configured serial ports for a parent resource  |
| `SerialPorts_ListBySubscriptions` | `SELECT` | `subscriptionId` | Handles requests to list all SerialPort resources in a subscription. |
| `SerialPorts_Create` | `INSERT` | `parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, serialPort, subscriptionId` | Creates or updates a serial port |
| `SerialPorts_Delete` | `DELETE` | `parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, serialPort, subscriptionId` | Deletes a serial port |
| `SerialPorts_Connect` | `EXEC` | `parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, serialPort, subscriptionId` | Connect to serial port of the target resource |
