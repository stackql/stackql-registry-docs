---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - tags
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.tags.tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="_type" /> | `string` | The type of object being created. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="label" /> | `string` | The label of the tag. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_entity_type_by_id_tags" /> | `SELECT` | <CopyableCode code="entity_type, id" /> | Get related tags for Users, Teams or Escalation Policies.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| <CopyableCode code="get_tag" /> | `SELECT` | <CopyableCode code="id" /> | Get details about an existing Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| <CopyableCode code="get_tags_by_entity_type" /> | `SELECT` | <CopyableCode code="entity_type, id" /> | Get related Users, Teams or Escalation Policies for the Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| <CopyableCode code="list_tags" /> | `SELECT` |  | List all of your account's tags.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| <CopyableCode code="create_entity_type_by_id_change_tags" /> | `INSERT` | <CopyableCode code="entity_type, id" /> | Assign existing or new tags.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.write`<br /> |
| <CopyableCode code="create_tags" /> | `INSERT` | <CopyableCode code="data__tag" /> | Create a Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.write`<br /> |
| <CopyableCode code="delete_tag" /> | `DELETE` | <CopyableCode code="id" /> | Remove an existing Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.write`<br /> |
| <CopyableCode code="_get_entity_type_by_id_tags" /> | `EXEC` | <CopyableCode code="entity_type, id" /> | Get related tags for Users, Teams or Escalation Policies.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| <CopyableCode code="_get_tag" /> | `EXEC` | <CopyableCode code="id" /> | Get details about an existing Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| <CopyableCode code="_get_tags_by_entity_type" /> | `EXEC` | <CopyableCode code="entity_type, id" /> | Get related Users, Teams or Escalation Policies for the Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| <CopyableCode code="_list_tags" /> | `EXEC` |  | List all of your account's tags.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
