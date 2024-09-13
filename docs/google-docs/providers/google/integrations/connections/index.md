
---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - integrations
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the Connection. Format: projects/{project}/locations/{location}/connections/{connection} |
| <CopyableCode code="description" /> | `string` | Optional. Description of the resource. |
| <CopyableCode code="asyncOperationsEnabled" /> | `boolean` | Optional. Async operations enabled for the connection. If Async Operations is enabled, Connection allows the customers to initiate async long running operations using the actions API. |
| <CopyableCode code="authConfig" /> | `object` | AuthConfig defines details of a authentication type. |
| <CopyableCode code="billingConfig" /> | `object` | Billing config for the connection. |
| <CopyableCode code="configVariables" /> | `array` | Optional. Configuration for configuring the connection with an external system. |
| <CopyableCode code="connectionRevision" /> | `string` | Output only. Connection revision. This field is only updated when the connection is created or updated by User. |
| <CopyableCode code="connectorVersion" /> | `string` | Required. Connector version on which the connection is created. The format is: projects/*/locations/*/providers/*/connectors/*/versions/* Only global location is supported for ConnectorVersion resource. |
| <CopyableCode code="connectorVersionInfraConfig" /> | `object` | This cofiguration provides infra configs like rate limit threshold which need to be configurable for every connector version |
| <CopyableCode code="connectorVersionLaunchStage" /> | `string` | Output only. Flag to mark the version indicating the launch stage. |
| <CopyableCode code="createTime" /> | `string` | Output only. Created time. |
| <CopyableCode code="destinationConfigs" /> | `array` | Optional. Configuration of the Connector's destination. Only accepted for Connectors that accepts user defined destination(s). |
| <CopyableCode code="envoyImageLocation" /> | `string` | Output only. GCR location where the envoy image is stored. formatted like: gcr.io/{bucketName}/{imageName} |
| <CopyableCode code="eventingConfig" /> | `object` | Eventing Configuration of a connection |
| <CopyableCode code="eventingEnablementType" /> | `string` | Optional. Eventing enablement type. Will be nil if eventing is not enabled. |
| <CopyableCode code="eventingRuntimeData" /> | `object` | Eventing runtime data has the details related to eventing managed by the system. |
| <CopyableCode code="host" /> | `string` | Output only. The name of the Hostname of the Service Directory service with TLS. |
| <CopyableCode code="imageLocation" /> | `string` | Output only. GCR location where the runtime image is stored. formatted like: gcr.io/{bucketName}/{imageName} |
| <CopyableCode code="isTrustedTester" /> | `boolean` | Output only. Is trusted tester program enabled for the project. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| <CopyableCode code="lockConfig" /> | `object` | Determines whether or no a connection is locked. If locked, a reason must be specified. |
| <CopyableCode code="logConfig" /> | `object` | Log configuration for the connection. |
| <CopyableCode code="nodeConfig" /> | `object` | Node configuration for the connection. |
| <CopyableCode code="serviceAccount" /> | `string` | Optional. Service account needed for runtime plane to access Google Cloud resources. |
| <CopyableCode code="serviceDirectory" /> | `string` | Output only. The name of the Service Directory service name. Used for Private Harpoon to resolve the ILB address. e.g. "projects/cloud-connectors-e2e-testing/locations/us-central1/namespaces/istio-system/services/istio-ingressgateway-connectors" |
| <CopyableCode code="sslConfig" /> | `object` | SSL Configuration of a connection |
| <CopyableCode code="status" /> | `object` | ConnectionStatus indicates the state of the connection. |
| <CopyableCode code="subscriptionType" /> | `string` | Output only. This subscription type enum states the subscription type of the project. |
| <CopyableCode code="suspended" /> | `boolean` | Optional. Suspended indicates if a user has suspended a connection or not. |
| <CopyableCode code="tlsMigrationState" /> | `string` | Output only. Status of the TLS migration. |
| <CopyableCode code="tlsServiceDirectory" /> | `string` | Output only. The name of the Service Directory service with TLS. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Updated time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_connections_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Connections in a given project and location. |

## `SELECT` examples

Lists Connections in a given project and location.

```sql
SELECT
name,
description,
asyncOperationsEnabled,
authConfig,
billingConfig,
configVariables,
connectionRevision,
connectorVersion,
connectorVersionInfraConfig,
connectorVersionLaunchStage,
createTime,
destinationConfigs,
envoyImageLocation,
eventingConfig,
eventingEnablementType,
eventingRuntimeData,
host,
imageLocation,
isTrustedTester,
labels,
lockConfig,
logConfig,
nodeConfig,
serviceAccount,
serviceDirectory,
sslConfig,
status,
subscriptionType,
suspended,
tlsMigrationState,
tlsServiceDirectory,
updateTime
FROM google.integrations.connections
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
