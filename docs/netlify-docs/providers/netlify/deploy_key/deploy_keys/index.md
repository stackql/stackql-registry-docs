---
title: deploy_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - deploy_keys
  - deploy_key
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deploy_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.deploy_key.deploy_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="public_key" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getDeployKey" /> | `SELECT` | <CopyableCode code="key_id" /> |
| <CopyableCode code="listDeployKeys" /> | `SELECT` |  |
| <CopyableCode code="createDeployKey" /> | `INSERT` |  |
| <CopyableCode code="deleteDeployKey" /> | `DELETE` | <CopyableCode code="key_id" /> |
