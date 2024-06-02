---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - metastore
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="metastore.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The relative resource name of the metastore service, in the following format:projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/services/&#123;service_id&#125;. |
| <CopyableCode code="artifactGcsUri" /> | `string` | Output only. A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the metastore service was created. |
| <CopyableCode code="databaseType" /> | `string` | Immutable. The database type that the Metastore service stores its data. |
| <CopyableCode code="deletionProtection" /> | `boolean` | Optional. Indicates if the dataproc metastore should be protected against accidental deletions. |
| <CopyableCode code="encryptionConfig" /> | `object` | Encryption settings for the service. |
| <CopyableCode code="endpointUri" /> | `string` | Output only. The URI of the endpoint used to access the metastore service. |
| <CopyableCode code="hiveMetastoreConfig" /> | `object` | Specifies configuration information specific to running Hive metastore software as the metastore service. |
| <CopyableCode code="labels" /> | `object` | User-defined labels for the metastore service. |
| <CopyableCode code="maintenanceWindow" /> | `object` | Maintenance window. This specifies when Dataproc Metastore may perform system maintenance operation to the service. |
| <CopyableCode code="metadataIntegration" /> | `object` | Specifies how metastore metadata should be integrated with external services. |
| <CopyableCode code="metadataManagementActivity" /> | `object` | The metadata management activities of the metastore service. |
| <CopyableCode code="network" /> | `string` | Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/&#123;project_number&#125;/global/networks/&#123;network_id&#125;. |
| <CopyableCode code="networkConfig" /> | `object` | Network configuration for the Dataproc Metastore service. |
| <CopyableCode code="port" /> | `integer` | The TCP port at which the metastore service is reached. Default: 9083. |
| <CopyableCode code="releaseChannel" /> | `string` | Immutable. The release channel of the service. If unspecified, defaults to STABLE. |
| <CopyableCode code="scalingConfig" /> | `object` | Represents the scaling configuration of a metastore service. |
| <CopyableCode code="scheduledBackup" /> | `object` | This specifies the configuration of scheduled backup. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the metastore service. |
| <CopyableCode code="stateMessage" /> | `string` | Output only. Additional information about the current state of the metastore service, if available. |
| <CopyableCode code="telemetryConfig" /> | `object` | Telemetry Configuration for the Dataproc Metastore service. |
| <CopyableCode code="tier" /> | `string` | The tier of the service. |
| <CopyableCode code="uid" /> | `string` | Output only. The globally unique resource identifier of the metastore service. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the metastore service was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Gets the details of a single service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists services in a project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a metastore service in a project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Deletes a single service. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists services in a project and location. |
| <CopyableCode code="alter_location" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location. |
| <CopyableCode code="alter_table_properties" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Alter metadata table properties. |
| <CopyableCode code="export_metadata" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Exports metadata from a service. |
| <CopyableCode code="move_table_to_database" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Move a table to another database. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Updates the parameters of a single service. |
| <CopyableCode code="query_metadata" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Query Dataproc Metastore metadata. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Restores a service from a backup. |
