---
title: autonomous_database_character_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_database_character_sets
  - oracledatabase
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

Creates, updates, deletes, gets or lists a <code>autonomous_database_character_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autonomous_database_character_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oracledatabase.autonomous_database_character_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of the Autonomous Database Character Set resource in the following format: projects/{project}/locations/{region}/autonomousDatabaseCharacterSets/{autonomous_database_character_set} |
| <CopyableCode code="characterSet" /> | `string` | Output only. The character set name for the Autonomous Database which is the ID in the resource name. |
| <CopyableCode code="characterSetType" /> | `string` | Output only. The character set type for the Autonomous Database. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Autonomous Database Character Sets in a given project and location. |

## `SELECT` examples

Lists Autonomous Database Character Sets in a given project and location.

```sql
SELECT
name,
characterSet,
characterSetType
FROM google.oracledatabase.autonomous_database_character_sets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
