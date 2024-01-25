---
title: locations_billing_specs
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_billing_specs
  - hdinsight
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
<tr><td><b>Name</b></td><td><code>locations_billing_specs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.locations_billing_specs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `billingResources` | `array` | The billing and managed disk billing resources for a region. |
| `vmSizeFilters` | `array` | The virtual machine filtering mode. Effectively this can enabling or disabling the virtual machine sizes in a particular set. |
| `vmSizeProperties` | `array` | The vm size properties. |
| `vmSizes` | `array` | The virtual machine sizes to include or exclude. |
| `vmSizesWithEncryptionAtHost` | `array` | The vm sizes which enable encryption at host. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `location, subscriptionId` |
