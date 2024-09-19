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
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: state
      value: string
    - name: displayName
      value: string
    - name: mysql
      value:
        - name: host
          value: string
        - name: port
          value: integer
        - name: username
          value: string
        - name: password
          value: string
        - name: passwordSet
          value: boolean
        - name: ssl
          value:
            - name: type
              value: string
            - name: clientKey
              value: string
            - name: clientCertificate
              value: string
            - name: caCertificate
              value: string
        - name: cloudSqlId
          value: string
    - name: postgresql
      value:
        - name: host
          value: string
        - name: port
          value: integer
        - name: username
          value: string
        - name: password
          value: string
        - name: passwordSet
          value: boolean
        - name: cloudSqlId
          value: string
        - name: alloydbClusterId
          value: string
        - name: networkArchitecture
          value: string
        - name: staticIpConnectivity
          value: []
        - name: privateServiceConnectConnectivity
          value:
            - name: serviceAttachment
              value: string
    - name: sqlserver
      value:
        - name: host
          value: string
        - name: port
          value: integer
        - name: username
          value: string
        - name: password
          value: string
        - name: passwordSet
          value: boolean
        - name: cloudSqlId
          value: string
        - name: backups
          value:
            - name: gcsBucket
              value: string
            - name: gcsPrefix
              value: string
        - name: forwardSshConnectivity
          value:
            - name: hostname
              value: string
            - name: username
              value: string
            - name: port
              value: integer
            - name: password
              value: string
            - name: privateKey
              value: string
        - name: privateConnectivity
          value:
            - name: privateConnection
              value: string
    - name: oracle
      value:
        - name: host
          value: string
        - name: port
          value: integer
        - name: username
          value: string
        - name: password
          value: string
        - name: passwordSet
          value: boolean
        - name: databaseService
          value: string
        - name: staticServiceIpConnectivity
          value: []
        - name: oracleAsmConfig
          value:
            - name: hostname
              value: string
            - name: port
              value: integer
            - name: username
              value: string
            - name: password
              value: string
            - name: passwordSet
              value: boolean
            - name: asmService
              value: string
    - name: cloudsql
      value:
        - name: cloudSqlId
          value: string
        - name: settings
          value:
            - name: databaseVersion
              value: string
            - name: userLabels
              value: object
            - name: tier
              value: string
            - name: storageAutoResizeLimit
              value: string
            - name: activationPolicy
              value: string
            - name: ipConfig
              value:
                - name: enableIpv4
                  value: boolean
                - name: privateNetwork
                  value: string
                - name: allocatedIpRange
                  value: string
                - name: requireSsl
                  value: boolean
                - name: authorizedNetworks
                  value:
                    - - name: value
                        value: string
                      - name: expireTime
                        value: string
                      - name: ttl
                        value: string
                      - name: label
                        value: string
            - name: autoStorageIncrease
              value: boolean
            - name: databaseFlags
              value: object
            - name: dataDiskType
              value: string
            - name: dataDiskSizeGb
              value: string
            - name: zone
              value: string
            - name: secondaryZone
              value: string
            - name: sourceId
              value: string
            - name: rootPassword
              value: string
            - name: rootPasswordSet
              value: boolean
            - name: collation
              value: string
            - name: cmekKeyName
              value: string
            - name: availabilityType
              value: string
            - name: edition
              value: string
            - name: dataCacheConfig
              value:
                - name: dataCacheEnabled
                  value: boolean
        - name: privateIp
          value: string
        - name: publicIp
          value: string
        - name: additionalPublicIp
          value: string
    - name: alloydb
      value:
        - name: clusterId
          value: string
        - name: settings
          value:
            - name: initialUser
              value:
                - name: user
                  value: string
                - name: password
                  value: string
                - name: passwordSet
                  value: boolean
            - name: vpcNetwork
              value: string
            - name: labels
              value: object
            - name: primaryInstanceSettings
              value:
                - name: id
                  value: string
                - name: machineConfig
                  value:
                    - name: cpuCount
                      value: integer
                - name: databaseFlags
                  value: object
                - name: labels
                  value: object
                - name: privateIp
                  value: string
            - name: encryptionConfig
              value:
                - name: kmsKeyName
                  value: string
            - name: databaseVersion
              value: string
    - name: error
      value:
        - name: code
          value: integer
        - name: message
          value: string
        - name: details
          value:
            - object
    - name: provider
      value: string

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
