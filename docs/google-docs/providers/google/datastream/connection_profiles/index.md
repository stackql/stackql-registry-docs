---
title: connection_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_profiles
  - datastream
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.datastream.connection_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource's name. |
| <CopyableCode code="bigqueryProfile" /> | `object` | BigQuery warehouse profile. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time of the resource. |
| <CopyableCode code="displayName" /> | `string` | Required. Display name. |
| <CopyableCode code="forwardSshConnectivity" /> | `object` | Forward SSH Tunnel connectivity. |
| <CopyableCode code="gcsProfile" /> | `object` | Cloud Storage bucket profile. |
| <CopyableCode code="labels" /> | `object` | Labels. |
| <CopyableCode code="mysqlProfile" /> | `object` | MySQL database profile. |
| <CopyableCode code="oracleProfile" /> | `object` | Oracle database profile. |
| <CopyableCode code="postgresqlProfile" /> | `object` | PostgreSQL database profile. |
| <CopyableCode code="privateConnectivity" /> | `object` | Private Connectivity |
| <CopyableCode code="sqlServerProfile" /> | `object` | SQLServer database profile |
| <CopyableCode code="staticServiceIpConnectivity" /> | `object` | Static IP address connectivity. Used when the source database is configured to allow incoming connections from the Datastream public IP addresses for the region specified in the connection profile. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update time of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionProfilesId, locationsId, projectsId" /> | Use this method to get details about a connection profile. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Use this method to list connection profiles created in a project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Use this method to create a connection profile in a project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionProfilesId, locationsId, projectsId" /> | Use this method to delete a connection profile. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="connectionProfilesId, locationsId, projectsId" /> | Use this method to update the parameters of a connection profile. |
| <CopyableCode code="discover" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request. |

## `SELECT` examples

Use this method to list connection profiles created in a project and location.

```sql
SELECT
name,
bigqueryProfile,
createTime,
displayName,
forwardSshConnectivity,
gcsProfile,
labels,
mysqlProfile,
oracleProfile,
postgresqlProfile,
privateConnectivity,
sqlServerProfile,
staticServiceIpConnectivity,
updateTime
FROM google.datastream.connection_profiles
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
INSERT INTO google.datastream.connection_profiles (
locationsId,
projectsId,
labels,
displayName,
oracleProfile,
gcsProfile,
mysqlProfile,
bigqueryProfile,
postgresqlProfile,
sqlServerProfile,
staticServiceIpConnectivity,
forwardSshConnectivity,
privateConnectivity
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ labels }}',
'{{ displayName }}',
'{{ oracleProfile }}',
'{{ gcsProfile }}',
'{{ mysqlProfile }}',
'{{ bigqueryProfile }}',
'{{ postgresqlProfile }}',
'{{ sqlServerProfile }}',
'{{ staticServiceIpConnectivity }}',
'{{ forwardSshConnectivity }}',
'{{ privateConnectivity }}'
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
    - name: displayName
      value: string
    - name: oracleProfile
      value:
        - name: hostname
          value: string
        - name: port
          value: integer
        - name: username
          value: string
        - name: password
          value: string
        - name: databaseService
          value: string
        - name: connectionAttributes
          value: object
        - name: oracleSslConfig
          value:
            - name: caCertificate
              value: string
            - name: caCertificateSet
              value: boolean
    - name: gcsProfile
      value:
        - name: bucket
          value: string
        - name: rootPath
          value: string
    - name: mysqlProfile
      value:
        - name: hostname
          value: string
        - name: port
          value: integer
        - name: username
          value: string
        - name: password
          value: string
        - name: sslConfig
          value:
            - name: clientKey
              value: string
            - name: clientKeySet
              value: boolean
            - name: clientCertificate
              value: string
            - name: clientCertificateSet
              value: boolean
            - name: caCertificate
              value: string
            - name: caCertificateSet
              value: boolean
    - name: bigqueryProfile
      value: []
    - name: postgresqlProfile
      value:
        - name: hostname
          value: string
        - name: port
          value: integer
        - name: username
          value: string
        - name: password
          value: string
        - name: database
          value: string
    - name: sqlServerProfile
      value:
        - name: hostname
          value: string
        - name: port
          value: integer
        - name: username
          value: string
        - name: password
          value: string
        - name: database
          value: string
    - name: staticServiceIpConnectivity
      value: []
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connection_profiles</code> resource.

```sql
/*+ update */
UPDATE google.datastream.connection_profiles
SET 
labels = '{{ labels }}',
displayName = '{{ displayName }}',
oracleProfile = '{{ oracleProfile }}',
gcsProfile = '{{ gcsProfile }}',
mysqlProfile = '{{ mysqlProfile }}',
bigqueryProfile = '{{ bigqueryProfile }}',
postgresqlProfile = '{{ postgresqlProfile }}',
sqlServerProfile = '{{ sqlServerProfile }}',
staticServiceIpConnectivity = '{{ staticServiceIpConnectivity }}',
forwardSshConnectivity = '{{ forwardSshConnectivity }}',
privateConnectivity = '{{ privateConnectivity }}'
WHERE 
connectionProfilesId = '{{ connectionProfilesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>connection_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM google.datastream.connection_profiles
WHERE connectionProfilesId = '{{ connectionProfilesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
