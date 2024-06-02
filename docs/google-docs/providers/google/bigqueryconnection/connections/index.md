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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="bigqueryconnection.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the connection in the form of: `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/connections/&#123;connection_id&#125;` |
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
| <CopyableCode code="kmsKeyName" /> | `string` | Optional. The Cloud KMS key that is used for encryption. Example: `projects/[kms_project_id]/locations/[region]/keyRings/[key_region]/cryptoKeys/[key]` |
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
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Returns a list of connections in the given project. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask. |
