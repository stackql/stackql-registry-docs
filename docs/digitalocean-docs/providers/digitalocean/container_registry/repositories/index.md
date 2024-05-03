---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
  - container_registry
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.container_registry.repositories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the repository. |
| <CopyableCode code="latest_tag" /> | `object` |  |
| <CopyableCode code="registry_name" /> | `string` | The name of the container registry. |
| <CopyableCode code="tag_count" /> | `integer` | The number of tags in the repository. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="registry_list_repositories" /> | `SELECT` | <CopyableCode code="registry_name" /> |
| <CopyableCode code="_registry_list_repositories" /> | `EXEC` | <CopyableCode code="registry_name" /> |
