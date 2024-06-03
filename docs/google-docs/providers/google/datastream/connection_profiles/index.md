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
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Use this method to list connection profiles created in a project and location. |
| <CopyableCode code="discover" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request. |
