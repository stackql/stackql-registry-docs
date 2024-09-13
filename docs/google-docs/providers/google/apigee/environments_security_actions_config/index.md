---
title: environments_security_actions_config
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_security_actions_config
  - apigee
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

Creates, updates, deletes, gets or lists a <code>environments_security_actions_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_security_actions_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.environments_security_actions_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | This is a singleton resource, the name will always be set by SecurityActions and any user input will be ignored. The name is always: `organizations/{org}/environments/{env}/security_actions_config` |
| <CopyableCode code="enabled" /> | `boolean` | The flag that controls whether this feature is enabled. This is `unset` by default. When this flag is `false`, even if individual rules are enabled, no SecurityActions will be enforced. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update time for configuration. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_get_security_actions_config" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | GetSecurityActionConfig returns the current SecurityActions configuration. |
| <CopyableCode code="organizations_environments_update_security_actions_config" /> | `UPDATE` | <CopyableCode code="environmentsId, organizationsId" /> | UpdateSecurityActionConfig updates the current SecurityActions configuration. This method is used to enable/disable the feature at the environment level. |

## `SELECT` examples

GetSecurityActionConfig returns the current SecurityActions configuration.

```sql
SELECT
name,
enabled,
updateTime
FROM google.apigee.environments_security_actions_config
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `UPDATE` example

Updates a <code>environments_security_actions_config</code> resource.

```sql
/*+ update */
UPDATE google.apigee.environments_security_actions_config
SET 
updateTime = '{{ updateTime }}',
name = '{{ name }}',
enabled = true|false
WHERE 
environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}';
```
