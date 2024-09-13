
---
title: groups_security_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - groups_security_settings
  - cloudidentity
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>groups_security_setting</code> resource or lists <code>groups_security_settings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups_security_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.groups_security_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the security settings. Shall be of the form `groups/{group_id}/securitySettings`. |
| <CopyableCode code="memberRestriction" /> | `object` | The definition of MemberRestriction |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_security_settings" /> | `SELECT` | <CopyableCode code="groupsId" /> | Get Security Settings |
| <CopyableCode code="update_security_settings" /> | `UPDATE` | <CopyableCode code="groupsId" /> | Update Security Settings |

## `SELECT` examples

Get Security Settings

```sql
SELECT
name,
memberRestriction
FROM google.cloudidentity.groups_security_settings
WHERE groupsId = '{{ groupsId }}'; 
```

## `UPDATE` example

Updates a groups_security_setting only if the necessary resources are available.

```sql
UPDATE google.cloudidentity.groups_security_settings
SET 
name = '{{ name }}',
memberRestriction = '{{ memberRestriction }}'
WHERE 
groupsId = '{{ groupsId }}';
```
