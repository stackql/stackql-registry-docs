---
title: databases_ddl
hide_title: false
hide_table_of_contents: false
keywords:
  - databases_ddl
  - spanner
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

Creates, updates, deletes, gets or lists a <code>databases_ddl</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases_ddl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.databases_ddl" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="protoDescriptors" /> | `string` | Proto descriptors stored in the database. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description). |
| <CopyableCode code="statements" /> | `array` | A list of formatted DDL statements defining the schema of the database specified in the request. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instances_databases_get_ddl" /> | `SELECT` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Returns the schema of a Cloud Spanner database as a list of formatted DDL statements. This method does not show pending schema updates, those may be queried using the Operations API. |
| <CopyableCode code="projects_instances_databases_update_ddl" /> | `UPDATE` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Updates the schema of a Cloud Spanner database by creating/altering/dropping tables, columns, indexes, etc. The returned long-running operation will have a name of the format `/operations/` and can be used to track execution of the schema change(s). The metadata field type is UpdateDatabaseDdlMetadata. The operation has no response. |

## `SELECT` examples

Returns the schema of a Cloud Spanner database as a list of formatted DDL statements. This method does not show pending schema updates, those may be queried using the Operations API.

```sql
SELECT
protoDescriptors,
statements
FROM google.spanner.databases_ddl
WHERE databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a <code>databases_ddl</code> resource.

```sql
/*+ update */
UPDATE google.spanner.databases_ddl
SET 
statements = '{{ statements }}',
operationId = '{{ operationId }}',
protoDescriptors = '{{ protoDescriptors }}'
WHERE 
databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```
