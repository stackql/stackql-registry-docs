---
title: instance_details
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_details
  - osconfig
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.osconfig.instance_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The instance name in the form `projects/*/zones/*/instances/*` |
| `state` | `string` | Current state of instance patch. |
| `attemptCount` | `string` | The number of times the agent that the agent attempts to apply the patch. |
| `failureReason` | `string` | If the patch fails, this field provides the reason. |
| `instanceSystemId` | `string` | The unique identifier for the instance. This identifier is defined by the server. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `patchJobsId, projectsId` |
| `_list` | `EXEC` | `patchJobsId, projectsId` |
