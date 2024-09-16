---
title: connection_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_profiles
  - datamigration
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

Creates, updates, deletes, gets or lists a <code>connection_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datamigration.connection_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of this connection profile resource in the form of projects/{project}/locations/{location}/connectionProfiles/{connectionProfile}. |
| <CopyableCode code="alloydb" /> | `object` | Specifies required connection parameters, and the parameters required to create an AlloyDB destination cluster. |
| <CopyableCode code="cloudsql" /> | `object` | Specifies required connection parameters, and, optionally, the parameters required to create a Cloud SQL destination database instance. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". |
| <CopyableCode code="displayName" /> | `string` | The connection profile display name. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="labels" /> | `object` | The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
| <CopyableCode code="mysql" /> | `object` | Specifies connection parameters required specifically for MySQL databases. |
| <CopyableCode code="oracle" /> | `object` | Specifies connection parameters required specifically for Oracle databases. |
| <CopyableCode code="postgresql" /> | `object` | Specifies connection parameters required specifically for PostgreSQL databases. |
| <CopyableCode code="provider" /> | `string` | The database provider. |
| <CopyableCode code="sqlserver" /> | `object` | Specifies connection parameters required specifically for SQL Server databases. |
| <CopyableCode code="state" /> | `string` | The current connection profile state (e.g. DRAFT, READY, or FAILED). |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionProfilesId, locationsId, projectsId" /> | Gets details of a single connection profile. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Retrieves a list of all connection profiles in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new connection profile in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionProfilesId, locationsId, projectsId" /> | Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="connectionProfilesId, locationsId, projectsId" /> | Update the configuration of a single connection profile. |

## `SELECT` examples

Retrieves a list of all connection profiles in a given project and location.

```sql
SELECT
name,
alloydb,
cloudsql,
createTime,
displayName,
error,
labels,
mysql,
oracle,
postgresql,
provider,
sqlserver,
state,
updateTime
FROM google.datamigration.connection_profiles
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connection_profiles</code> resource.

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
INSERT INTO google.datamigration.connection_profiles (
locationsId,
projectsId,
name,
labels,
state,
displayName,
mysql,
postgresql,
sqlserver,
oracle,
cloudsql,
alloydb,
provider
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ state }}',
'{{ displayName }}',
'{{ mysql }}',
'{{ postgresql }}',
'{{ sqlserver }}',
'{{ oracle }}',
'{{ cloudsql }}',
'{{ alloydb }}',
'{{ provider }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: labels
      value: '{{ labels }}'
    - name: state
      value: '{{ state }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: mysql
      value:
        - name: host
          value: '{{ host }}'
        - name: port
          value: '{{ port }}'
        - name: username
          value: '{{ username }}'
        - name: password
          value: '{{ password }}'
        - name: ssl
          value:
            - name: clientKey
              value: '{{ clientKey }}'
            - name: clientCertificate
              value: '{{ clientCertificate }}'
            - name: caCertificate
              value: '{{ caCertificate }}'
        - name: cloudSqlId
          value: '{{ cloudSqlId }}'
    - name: postgresql
      value:
        - name: host
          value: '{{ host }}'
        - name: port
          value: '{{ port }}'
        - name: username
          value: '{{ username }}'
        - name: password
          value: '{{ password }}'
        - name: cloudSqlId
          value: '{{ cloudSqlId }}'
        - name: alloydbClusterId
          value: '{{ alloydbClusterId }}'
        - name: staticIpConnectivity
          value: []
        - name: privateServiceConnectConnectivity
          value:
            - name: serviceAttachment
              value: '{{ serviceAttachment }}'
    - name: sqlserver
      value:
        - name: host
          value: '{{ host }}'
        - name: port
          value: '{{ port }}'
        - name: username
          value: '{{ username }}'
        - name: password
          value: '{{ password }}'
        - name: cloudSqlId
          value: '{{ cloudSqlId }}'
        - name: backups
          value:
            - name: gcsBucket
              value: '{{ gcsBucket }}'
            - name: gcsPrefix
              value: '{{ gcsPrefix }}'
        - name: forwardSshConnectivity
          value:
            - name: hostname
              value: '{{ hostname }}'
            - name: username
              value: '{{ username }}'
            - name: port
              value: '{{ port }}'
            - name: password
              value: '{{ password }}'
            - name: privateKey
              value: '{{ privateKey }}'
        - name: privateConnectivity
          value:
            - name: privateConnection
              value: '{{ privateConnection }}'
    - name: oracle
      value:
        - name: host
          value: '{{ host }}'
        - name: port
          value: '{{ port }}'
        - name: username
          value: '{{ username }}'
        - name: password
          value: '{{ password }}'
        - name: databaseService
          value: '{{ databaseService }}'
        - name: staticServiceIpConnectivity
          value: []
        - name: oracleAsmConfig
          value:
            - name: hostname
              value: '{{ hostname }}'
            - name: port
              value: '{{ port }}'
            - name: username
              value: '{{ username }}'
            - name: password
              value: '{{ password }}'
            - name: asmService
              value: '{{ asmService }}'
    - name: cloudsql
      value:
        - name: settings
          value:
            - name: databaseVersion
              value: '{{ databaseVersion }}'
            - name: userLabels
              value: '{{ userLabels }}'
            - name: tier
              value: '{{ tier }}'
            - name: storageAutoResizeLimit
              value: '{{ storageAutoResizeLimit }}'
            - name: activationPolicy
              value: '{{ activationPolicy }}'
            - name: ipConfig
              value:
                - name: enableIpv4
                  value: '{{ enableIpv4 }}'
                - name: privateNetwork
                  value: '{{ privateNetwork }}'
                - name: allocatedIpRange
                  value: '{{ allocatedIpRange }}'
                - name: requireSsl
                  value: '{{ requireSsl }}'
                - name: authorizedNetworks
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
            - name: autoStorageIncrease
              value: '{{ autoStorageIncrease }}'
            - name: databaseFlags
              value: '{{ databaseFlags }}'
            - name: dataDiskType
              value: '{{ dataDiskType }}'
            - name: dataDiskSizeGb
              value: '{{ dataDiskSizeGb }}'
            - name: zone
              value: '{{ zone }}'
            - name: secondaryZone
              value: '{{ secondaryZone }}'
            - name: sourceId
              value: '{{ sourceId }}'
            - name: rootPassword
              value: '{{ rootPassword }}'
            - name: collation
              value: '{{ collation }}'
            - name: cmekKeyName
              value: '{{ cmekKeyName }}'
            - name: availabilityType
              value: '{{ availabilityType }}'
            - name: edition
              value: '{{ edition }}'
            - name: dataCacheConfig
              value:
                - name: dataCacheEnabled
                  value: '{{ dataCacheEnabled }}'
    - name: alloydb
      value:
        - name: clusterId
          value: '{{ clusterId }}'
        - name: settings
          value:
            - name: initialUser
              value:
                - name: user
                  value: '{{ user }}'
                - name: password
                  value: '{{ password }}'
            - name: vpcNetwork
              value: '{{ vpcNetwork }}'
            - name: labels
              value: '{{ labels }}'
            - name: primaryInstanceSettings
              value:
                - name: machineConfig
                  value:
                    - name: cpuCount
                      value: '{{ cpuCount }}'
                - name: databaseFlags
                  value: '{{ databaseFlags }}'
                - name: labels
                  value: '{{ labels }}'
            - name: encryptionConfig
              value:
                - name: kmsKeyName
                  value: '{{ kmsKeyName }}'
            - name: databaseVersion
              value: '{{ databaseVersion }}'
    - name: provider
      value: '{{ provider }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connection_profiles</code> resource.

```sql
/*+ update */
UPDATE google.datamigration.connection_profiles
SET 
name = '{{ name }}',
labels = '{{ labels }}',
state = '{{ state }}',
displayName = '{{ displayName }}',
mysql = '{{ mysql }}',
postgresql = '{{ postgresql }}',
sqlserver = '{{ sqlserver }}',
oracle = '{{ oracle }}',
cloudsql = '{{ cloudsql }}',
alloydb = '{{ alloydb }}',
provider = '{{ provider }}'
WHERE 
connectionProfilesId = '{{ connectionProfilesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>connection_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM google.datamigration.connection_profiles
WHERE connectionProfilesId = '{{ connectionProfilesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
