---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - sqladmin
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

Creates, updates, deletes, gets or lists a <code>databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the database in the Cloud SQL instance. This does not include the project ID or instance name. |
| <CopyableCode code="charset" /> | `string` | The Cloud SQL charset value. |
| <CopyableCode code="collation" /> | `string` | The Cloud SQL collation value. |
| <CopyableCode code="etag" /> | `string` | This field is deprecated and will be removed from a future version of the API. |
| <CopyableCode code="instance" /> | `string` | The name of the Cloud SQL instance. This does not include the project ID. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#database`. |
| <CopyableCode code="project" /> | `string` | The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable. |
| <CopyableCode code="selfLink" /> | `string` | The URI of this resource. |
| <CopyableCode code="sqlserverDatabaseDetails" /> | `object` | Represents a Sql Server database on the Cloud SQL instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="database, instance, project" /> | Retrieves a resource containing information about a database inside a Cloud SQL instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instance, project" /> | Lists databases in the specified Cloud SQL instance. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="instance, project" /> | Inserts a resource containing information about a database inside a Cloud SQL instance. **Note:** You can't modify the default character set and collation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="database, instance, project" /> | Deletes a database from a Cloud SQL instance. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="database, instance, project" /> | Partially updates a resource containing information about a database inside a Cloud SQL instance. This method supports patch semantics. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="database, instance, project" /> | Updates a resource containing information about a database inside a Cloud SQL instance. |

## `SELECT` examples

Lists databases in the specified Cloud SQL instance.

```sql
SELECT
name,
charset,
collation,
etag,
instance,
kind,
project,
selfLink,
sqlserverDatabaseDetails
FROM google.sqladmin.databases
WHERE instance = '{{ instance }}'
AND project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>databases</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.sqladmin.databases (
instance,
project,
kind,
charset,
collation,
etag,
name,
instance,
selfLink,
project,
sqlserverDatabaseDetails
)
SELECT 
'{{ instance }}',
'{{ project }}',
'{{ kind }}',
'{{ charset }}',
'{{ collation }}',
'{{ etag }}',
'{{ name }}',
'{{ instance }}',
'{{ selfLink }}',
'{{ project }}',
'{{ sqlserverDatabaseDetails }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: '{{ kind }}'
    - name: charset
      value: '{{ charset }}'
    - name: collation
      value: '{{ collation }}'
    - name: etag
      value: '{{ etag }}'
    - name: name
      value: '{{ name }}'
    - name: instance
      value: '{{ instance }}'
    - name: selfLink
      value: '{{ selfLink }}'
    - name: project
      value: '{{ project }}'
    - name: sqlserverDatabaseDetails
      value: '{{ sqlserverDatabaseDetails }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>databases</code> resource.

```sql
/*+ update */
UPDATE google.sqladmin.databases
SET 
kind = '{{ kind }}',
charset = '{{ charset }}',
collation = '{{ collation }}',
etag = '{{ etag }}',
name = '{{ name }}',
instance = '{{ instance }}',
selfLink = '{{ selfLink }}',
project = '{{ project }}',
sqlserverDatabaseDetails = '{{ sqlserverDatabaseDetails }}'
WHERE 
database = '{{ database }}'
AND instance = '{{ instance }}'
AND project = '{{ project }}';
```

## `UPDATE` example

Replaces all fields in the specified <code>databases</code> resource.

```sql
/*+ update */
REPLACE google.sqladmin.databases
SET 
kind = '{{ kind }}',
charset = '{{ charset }}',
collation = '{{ collation }}',
etag = '{{ etag }}',
name = '{{ name }}',
instance = '{{ instance }}',
selfLink = '{{ selfLink }}',
project = '{{ project }}',
sqlserverDatabaseDetails = '{{ sqlserverDatabaseDetails }}'
WHERE 
database = '{{ database }}'
AND instance = '{{ instance }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified <code>databases</code> resource.

```sql
/*+ delete */
DELETE FROM google.sqladmin.databases
WHERE database = '{{ database }}'
AND instance = '{{ instance }}'
AND project = '{{ project }}';
```
