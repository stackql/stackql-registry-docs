---
title: pretargeting_configs_targeted_publishers
hide_title: false
hide_table_of_contents: false
keywords:
  - pretargeting_configs_targeted_publishers
  - realtimebidding
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pretargeting_configs_targeted_publishers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.realtimebidding.pretargeting_configs_targeted_publishers</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bidders_pretargetingConfigs_addTargetedPublishers` | `EXEC` | `biddersId, pretargetingConfigsId` | Adds targeted publishers to the pretargeting config. |
| `bidders_pretargetingConfigs_removeTargetedPublishers` | `EXEC` | `biddersId, pretargetingConfigsId` | Removes targeted publishers from the pretargeting config. |
