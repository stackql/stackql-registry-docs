---
title: test_job_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - test_job_streams
  - automation
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
<tr><td><b>Name</b></td><td><code>test_job_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.test_job_streams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the id of the resource. |
| `properties` | `object` | Definition of the job stream. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TestJobStreams_Get` | `SELECT` | `automationAccountName, jobStreamId, resourceGroupName, runbookName, subscriptionId` | Retrieve a test job stream of the test job identified by runbook name and stream id. |
| `TestJobStreams_ListByTestJob` | `SELECT` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Retrieve a list of test job streams identified by runbook name. |
