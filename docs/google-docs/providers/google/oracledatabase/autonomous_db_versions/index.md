---
title: autonomous_db_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_db_versions
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

Creates, updates, deletes, gets or lists a <code>autonomous_db_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autonomous_db_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oracledatabase.autonomous_db_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of the Autonomous Database Version resource with the format: projects/{project}/locations/{region}/autonomousDbVersions/{autonomous_db_version} |
| <CopyableCode code="dbWorkload" /> | `string` | Output only. The Autonomous Database workload type. |
| <CopyableCode code="version" /> | `string` | Output only. An Oracle Database version for Autonomous Database. |
| <CopyableCode code="workloadUri" /> | `string` | Output only. A URL that points to a detailed description of the Autonomous Database version. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the available Autonomous Database versions for a project and location. |

## `SELECT` examples

Lists all the available Autonomous Database versions for a project and location.

```sql
SELECT
name,
dbWorkload,
version,
workloadUri
FROM google.oracledatabase.autonomous_db_versions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
