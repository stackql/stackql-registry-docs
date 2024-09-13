---
title: supported_database_flags
hide_title: false
hide_table_of_contents: false
keywords:
  - supported_database_flags
  - alloydb
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

Creates, updates, deletes or gets an <code>supported_database_flag</code> resource or lists <code>supported_database_flags</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>supported_database_flags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.alloydb.supported_database_flags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the flag resource, following Google Cloud conventions, e.g.: * projects/{project}/locations/{location}/flags/{flag} This field currently has no semantic meaning. |
| <CopyableCode code="acceptsMultipleValues" /> | `boolean` | Whether the database flag accepts multiple values. If true, a comma-separated list of stringified values may be specified. |
| <CopyableCode code="flagName" /> | `string` | The name of the database flag, e.g. "max_allowed_packets". The is a possibly key for the Instance.database_flags map field. |
| <CopyableCode code="integerRestrictions" /> | `object` | Restrictions on INTEGER type values. |
| <CopyableCode code="requiresDbRestart" /> | `boolean` | Whether setting or updating this flag on an Instance requires a database restart. If a flag that requires database restart is set, the backend will automatically restart the database (making sure to satisfy any availability SLO's). |
| <CopyableCode code="stringRestrictions" /> | `object` | Restrictions on STRING type values |
| <CopyableCode code="supportedDbVersions" /> | `array` | Major database engine versions for which this flag is supported. |
| <CopyableCode code="valueType" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists SupportedDatabaseFlags for a given project and location. |

## `SELECT` examples

Lists SupportedDatabaseFlags for a given project and location.

```sql
SELECT
name,
acceptsMultipleValues,
flagName,
integerRestrictions,
requiresDbRestart,
stringRestrictions,
supportedDbVersions,
valueType
FROM google.alloydb.supported_database_flags
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
