---
title: region_commitments
hide_title: false
hide_table_of_contents: false
keywords:
  - region_commitments
  - compute
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
<tr><td><b>Name</b></td><td><code>region_commitments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_commitments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `mergeSourceCommitments` | `array` | List of source commitments to be merged into a new commitment. |
| `status` | `string` | [Output Only] Status of the commitment with regards to eventual expiration (each commitment has an end date defined). One of the following values: NOT_YET_ACTIVE, ACTIVE, EXPIRED. |
| `statusMessage` | `string` | [Output Only] An optional, human-readable explanation of the status. |
| `splitSourceCommitment` | `string` | Source commitment to be split into a new commitment. |
| `type` | `string` | The type of commitment, which affects the discount rate and the eligible resources. Type MEMORY_OPTIMIZED specifies a commitment that will only apply to memory optimized machines. Type ACCELERATOR_OPTIMIZED specifies a commitment that will only apply to accelerator optimized machines. |
| `endTimestamp` | `string` | [Output Only] Commitment end time in RFC3339 text format. |
| `category` | `string` | The category of the commitment. Category MACHINE specifies commitments composed of machine resources such as VCPU or MEMORY, listed in resources. Category LICENSE specifies commitments composed of software licenses, listed in licenseResources. Note that only MACHINE commitments should have a Type specified. |
| `licenseResource` | `object` | Commitment for a particular license resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `resources` | `array` | A list of commitment amounts for particular resources. Note that VCPU and MEMORY resource commitments must occur together. |
| `region` | `string` | [Output Only] URL of the region where this commitment may be used. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#commitment for commitments. |
| `plan` | `string` | The plan for this commitment, which determines duration and discount rate. The currently supported plans are TWELVE_MONTH (1 year), and THIRTY_SIX_MONTH (3 years). |
| `startTimestamp` | `string` | [Output Only] Commitment start time in RFC3339 text format. |
| `autoRenew` | `boolean` | Specifies whether to enable automatic renewal for the commitment. The default value is false if not specified. The field can be updated until the day of the commitment expiration at 12:00am PST. If the field is set to true, the commitment will be automatically renewed for either one or three years according to the terms of the existing commitment. |
| `reservations` | `array` | List of reservations in this commitment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregated_list` | `SELECT` | `project` | Retrieves an aggregated list of commitments by region. |
| `get` | `SELECT` | `commitment, project, region` | Returns the specified commitment resource. |
| `list` | `SELECT` | `project, region` | Retrieves a list of commitments contained within the specified region. |
| `insert` | `INSERT` | `project, region` | Creates a commitment in the specified project using the data included in the request. |
| `_aggregated_list` | `EXEC` | `project` | Retrieves an aggregated list of commitments by region. |
| `update` | `EXEC` | `commitment, project, region` | Updates the specified commitment with the data included in the request. Update is performed only on selected fields included as part of update-mask. Only the following fields can be modified: auto_renew. |
