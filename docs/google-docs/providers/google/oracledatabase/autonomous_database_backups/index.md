---
title: autonomous_database_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_database_backups
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

Creates, updates, deletes, gets or lists a <code>autonomous_database_backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autonomous_database_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oracledatabase.autonomous_database_backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of the Autonomous Database Backup resource with the format: projects/{project}/locations/{region}/autonomousDatabaseBackups/{autonomous_database_backup} |
| <CopyableCode code="autonomousDatabase" /> | `string` | Required. The name of the Autonomous Database resource for which the backup is being created. Format: projects/{project}/locations/{region}/autonomousDatabases/{autonomous_database} |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly name for the Backup. The name does not have to be unique. |
| <CopyableCode code="labels" /> | `object` | Optional. labels or tags associated with the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the Autonomous Database Backup resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the long term and automatic backups of an Autonomous Database. |

## `SELECT` examples

Lists the long term and automatic backups of an Autonomous Database.

```sql
SELECT
name,
autonomousDatabase,
displayName,
labels,
properties
FROM google.oracledatabase.autonomous_database_backups
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
