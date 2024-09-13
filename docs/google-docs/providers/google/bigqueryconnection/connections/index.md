
---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - bigqueryconnection
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

Creates, updates, deletes or gets an <code>connection</code> resource or lists <code>connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigqueryconnection.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/connections/{connection_id}` |
| <CopyableCode code="description" /> | `string` | User provided description. |
| <CopyableCode code="aws" /> | `object` | Connection properties specific to Amazon Web Services (AWS). |
| <CopyableCode code="azure" /> | `object` | Container for connection properties specific to Azure. |
| <CopyableCode code="cloudResource" /> | `object` | Container for connection properties for delegation of access to GCP resources. |
| <CopyableCode code="cloudSpanner" /> | `object` | Connection properties specific to Cloud Spanner. |
| <CopyableCode code="cloudSql" /> | `object` | Connection properties specific to the Cloud SQL. |
| <CopyableCode code="configuration" /> | `object` | Represents concrete parameter values for Connector Configuration. |
| <CopyableCode code="creationTime" /> | `string` | Output only. The creation timestamp of the connection. |
| <CopyableCode code="friendlyName" /> | `string` | User provided display name for the connection. |
| <CopyableCode code="hasCredential" /> | `boolean` | Output only. True, if credential is configured for this connection. |
| <CopyableCode code="kmsKeyName" /> | `string` | Optional. The Cloud KMS key that is used for credentials encryption. If omitted, internal Google owned encryption keys are used. Example: `projects/[kms_project_id]/locations/[region]/keyRings/[key_region]/cryptoKeys/[key]` |
| <CopyableCode code="lastModifiedTime" /> | `string` | Output only. The last update timestamp of the connection. |
| <CopyableCode code="salesforceDataCloud" /> | `object` | Connection properties specific to Salesforce DataCloud. This is intended for use only by Salesforce partner projects. |
| <CopyableCode code="spark" /> | `object` | Container for connection properties to execute stored procedures for Apache Spark. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Returns specified connection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns a list of connections in the given project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Deletes connection and associated credential. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask. |

## `SELECT` examples

Returns a list of connections in the given project.

```sql
SELECT
name,
description,
aws,
azure,
cloudResource,
cloudSpanner,
cloudSql,
configuration,
creationTime,
friendlyName,
hasCredential,
kmsKeyName,
lastModifiedTime,
salesforceDataCloud,
spark
FROM google.bigqueryconnection.connections
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connections</code> resource.

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
INSERT INTO google.bigqueryconnection.connections (
locationsId,
projectsId,
name,
friendlyName,
description,
cloudSql,
aws,
azure,
cloudSpanner,
cloudResource,
spark,
salesforceDataCloud,
configuration,
creationTime,
lastModifiedTime,
hasCredential,
kmsKeyName
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ friendlyName }}',
'{{ description }}',
'{{ cloudSql }}',
'{{ aws }}',
'{{ azure }}',
'{{ cloudSpanner }}',
'{{ cloudResource }}',
'{{ spark }}',
'{{ salesforceDataCloud }}',
'{{ configuration }}',
'{{ creationTime }}',
'{{ lastModifiedTime }}',
true|false,
'{{ kmsKeyName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: friendlyName
        value: '{{ friendlyName }}'
      - name: description
        value: '{{ description }}'
      - name: cloudSql
        value: '{{ cloudSql }}'
      - name: aws
        value: '{{ aws }}'
      - name: azure
        value: '{{ azure }}'
      - name: cloudSpanner
        value: '{{ cloudSpanner }}'
      - name: cloudResource
        value: '{{ cloudResource }}'
      - name: spark
        value: '{{ spark }}'
      - name: salesforceDataCloud
        value: '{{ salesforceDataCloud }}'
      - name: configuration
        value: '{{ configuration }}'
      - name: creationTime
        value: '{{ creationTime }}'
      - name: lastModifiedTime
        value: '{{ lastModifiedTime }}'
      - name: hasCredential
        value: '{{ hasCredential }}'
      - name: kmsKeyName
        value: '{{ kmsKeyName }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a connection only if the necessary resources are available.

```sql
UPDATE google.bigqueryconnection.connections
SET 
name = '{{ name }}',
friendlyName = '{{ friendlyName }}',
description = '{{ description }}',
cloudSql = '{{ cloudSql }}',
aws = '{{ aws }}',
azure = '{{ azure }}',
cloudSpanner = '{{ cloudSpanner }}',
cloudResource = '{{ cloudResource }}',
spark = '{{ spark }}',
salesforceDataCloud = '{{ salesforceDataCloud }}',
configuration = '{{ configuration }}',
creationTime = '{{ creationTime }}',
lastModifiedTime = '{{ lastModifiedTime }}',
hasCredential = true|false,
kmsKeyName = '{{ kmsKeyName }}'
WHERE 
connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified connection resource.

```sql
DELETE FROM google.bigqueryconnection.connections
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
