---
title: target_pools_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - target_pools_instance
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_pools_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.target_pools_instance" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_instance" /> | `EXEC` | <CopyableCode code="project, region, targetPool" /> | Adds an instance to a target pool. |
| <CopyableCode code="remove_instance" /> | `EXEC` | <CopyableCode code="project, region, targetPool" /> | Removes instance URL from a target pool. |
