---
title: troubleshooters
hide_title: false
hide_table_of_contents: false
keywords:
  - troubleshooters
  - help
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
<tr><td><b>Name</b></td><td><code>troubleshooters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.help.troubleshooters</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `scope, troubleshooterName` | Gets troubleshooter instance result which includes the step status/result of the troubleshooter resource name that is being executed.&lt;br/&gt; Get API is used to retrieve the result of a Troubleshooter instance, which includes the status and result of each step in the Troubleshooter workflow. This API requires the Troubleshooter resource name that was created using the Create API. |
| `create` | `INSERT` | `scope, troubleshooterName` | Creates the specific troubleshooter action under a resource or subscription using the ‘solutionId’ and  ‘properties.parameters’ as the trigger. &lt;br/&gt; Azure Troubleshooters help with hard to classify issues, reducing the gap between customer observed problems and solutions by guiding the user effortlessly through the troubleshooting process. Each Troubleshooter flow represents a problem area within Azure and has a complex tree-like structure that addresses many root causes. These flows are prepared with the help of Subject Matter experts and customer support engineers by carefully considering previous support requests raised by customers. Troubleshooters terminate at a well curated solution based off of resource backend signals and customer manual selections. |
| `continue` | `EXEC` | `scope, troubleshooterName` | Uses ‘stepId’ and ‘responses’ as the trigger to continue the troubleshooting steps for the respective troubleshooter resource name. &lt;br/&gt;Continue API is used to provide inputs that are required for the specific troubleshooter to progress into the next step in the process. This API is used after the Troubleshooter has been created using the Create API. |
| `end` | `EXEC` | `scope, troubleshooterName` | Ends the troubleshooter action |
| `restart` | `EXEC` | `scope, troubleshooterName` | Restarts the troubleshooter API using applicable troubleshooter resource name as the input.&lt;br/&gt; It returns new resource name which should be used in subsequent request. The old resource name is obsolete after this API is invoked. |
