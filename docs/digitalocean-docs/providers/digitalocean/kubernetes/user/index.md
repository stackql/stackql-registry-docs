---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - kubernetes
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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.user" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="groups" /> | `array` | A list of in-cluster groups that the user belongs to. |
| <CopyableCode code="username" /> | `string` | The username for the cluster admin user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_clusterUser" /> | `SELECT` | <CopyableCode code="cluster_id" /> |
| <CopyableCode code="_get_clusterUser" /> | `EXEC` | <CopyableCode code="cluster_id" /> |
