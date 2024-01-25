---
title: test_results
hide_title: false
hide_table_of_contents: false
keywords:
  - test_results
  - test_base
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>test_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.test_results</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName, testResultName` | Get the Test Result by Id with specified OS Update type for a Test Base Package. |
| `list` | `SELECT` | `osUpdateType, packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the Test Results with specified OS Update type for a Test Base Package. Can be filtered by osName, releaseName, flightingRing, buildVersion, buildRevision. |
| `_list` | `EXEC` | `osUpdateType, packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the Test Results with specified OS Update type for a Test Base Package. Can be filtered by osName, releaseName, flightingRing, buildVersion, buildRevision. |
