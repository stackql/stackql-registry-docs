---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - tags
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.tags.tags" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getTags" /> | `SELECT` |  | Tags are User-defined labels attached to objects in your Account, such as Linodes. They are used for specifying and grouping attributes of objects that are relevant to the User.<br /><br />This endpoint returns a paginated list of Tags on your account.<br /> |
| <CopyableCode code="createTag" /> | `INSERT` | <CopyableCode code="data__label" /> | Creates a new Tag and optionally tags requested objects with it immediately.<br /><br />**Important**: You must be an unrestricted User in order to add or modify Tags.<br /> |
| <CopyableCode code="deleteTag" /> | `DELETE` | <CopyableCode code="label" /> | Remove a Tag from all objects and delete it.<br /><br />**Important**: You must be an unrestricted User in order to add or modify Tags.<br /> |
| <CopyableCode code="_getTags" /> | `EXEC` |  | Tags are User-defined labels attached to objects in your Account, such as Linodes. They are used for specifying and grouping attributes of objects that are relevant to the User.<br /><br />This endpoint returns a paginated list of Tags on your account.<br /> |
