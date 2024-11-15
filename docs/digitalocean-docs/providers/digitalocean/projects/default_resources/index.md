---
title: default_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - default_resources
  - projects
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>default_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>default_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.projects.default_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="assigned_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the project was created. |
| <CopyableCode code="links" /> | `object` | The links object contains the `self` object, which contains the resource relationship. |
| <CopyableCode code="status" /> | `string` | The status of assigning and fetching the resources. |
| <CopyableCode code="urn" /> | `string` | The uniform resource name (URN) for the resource in the format do:resource_type:resource_id. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_list_resources_default" /> | `SELECT` | <CopyableCode code="" /> | To list all your resources in your default project, send a GET request to `/v2/projects/default/resources`. |
| <CopyableCode code="projects_assign_resources_default" /> | `EXEC` | <CopyableCode code="" /> | To assign resources to your default project, send a POST request to `/v2/projects/default/resources`. |

## `SELECT` examples

To list all your resources in your default project, send a GET request to `/v2/projects/default/resources`.


```sql
SELECT
assigned_at,
links,
status,
urn
FROM digitalocean.projects.default_resources
;
```