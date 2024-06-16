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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serial_ports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.serial_console.serial_ports" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, serialPort, subscriptionId" /> | Gets the configured settings for a serial port |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, subscriptionId" /> | Lists all of the configured serial ports for a parent resource  |
| <CopyableCode code="list_by_subscriptions" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Handles requests to list all SerialPort resources in a subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, serialPort, subscriptionId" /> | Creates or updates a serial port |
| <CopyableCode code="connect" /> | `EXEC` | <CopyableCode code="parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, serialPort, subscriptionId" /> | Connect to serial port of the target resource |
