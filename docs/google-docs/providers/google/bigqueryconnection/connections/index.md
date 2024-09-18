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

Creates, updates, deletes, gets or lists a <code>connections</code> resource.

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
kmsKeyName
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
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
'{{ kmsKeyName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
friendlyName: string
description: string
cloudSql:
  instanceId: string
  database: string
  type: string
  credential:
    username: string
    password: string
  serviceAccountId: string
aws:
  accessRole:
    iamRoleId: string
    identity: string
azure:
  application: string
  clientId: string
  objectId: string
  customerTenantId: string
  redirectUri: string
  federatedApplicationClientId: string
  identity: string
cloudSpanner:
  database: string
  useParallelism: boolean
  maxParallelism: integer
  useServerlessAnalytics: boolean
  useDataBoost: boolean
  databaseRole: string
cloudResource:
  serviceAccountId: string
spark:
  serviceAccountId: string
  metastoreServiceConfig:
    metastoreService: string
  sparkHistoryServerConfig:
    dataprocCluster: string
salesforceDataCloud:
  instanceUri: string
  identity: string
  tenantId: string
configuration:
  connectorId: string
  endpoint:
    hostPort: string
  authentication:
    usernamePassword:
      username: string
      password:
        plaintext: string
        secretType: string
    serviceAccount: string
  network:
    privateServiceConnect:
      networkAttachment: string
  asset:
    database: string
    googleCloudResource: string
creationTime: string
lastModifiedTime: string
hasCredential: boolean
kmsKeyName: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connections</code> resource.

```sql
/*+ update */
UPDATE google.bigqueryconnection.connections
SET 
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
kmsKeyName = '{{ kmsKeyName }}'
WHERE 
connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>connections</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigqueryconnection.connections
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
