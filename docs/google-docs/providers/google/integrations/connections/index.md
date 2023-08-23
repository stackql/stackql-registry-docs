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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.integrations.connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the Connection. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/connections/&#123;connection&#125; |
| `description` | `string` | Optional. Description of the resource. |
| `eventingRuntimeData` | `object` | Eventing runtime data has the details related to eventing managed by the system. |
| `sslConfig` | `object` | SSL Configuration of a connection |
| `updateTime` | `string` | Output only. Updated time. |
| `nodeConfig` | `object` | Node configuration for the connection. |
| `imageLocation` | `string` | Output only. GCR location where the runtime image is stored. formatted like: gcr.io/&#123;bucketName&#125;/&#123;imageName&#125; |
| `eventingConfig` | `object` | Eventing Configuration of a connection |
| `connectorVersionLaunchStage` | `string` | Output only. Flag to mark the version indicating the launch stage. |
| `serviceAccount` | `string` | Optional. Service account needed for runtime plane to access Google Cloud resources. |
| `lockConfig` | `object` | Determines whether or no a connection is locked. If locked, a reason must be specified. |
| `subscriptionType` | `string` | Output only. This subscription type enum states the subscription type of the project. |
| `envoyImageLocation` | `string` | Output only. GCR location where the envoy image is stored. formatted like: gcr.io/&#123;bucketName&#125;/&#123;imageName&#125; |
| `destinationConfigs` | `array` | Optional. Configuration of the Connector's destination. Only accepted for Connectors that accepts user defined destination(s). |
| `logConfig` | `object` | Log configuration for the connection. |
| `serviceDirectory` | `string` | Output only. The name of the Service Directory service name. Used for Private Harpoon to resolve the ILB address. e.g. "projects/cloud-connectors-e2e-testing/locations/us-central1/namespaces/istio-system/services/istio-ingressgateway-connectors" |
| `suspended` | `boolean` | Optional. Suspended indicates if a user has suspended a connection or not. |
| `eventingEnablementType` | `string` | Optional. Eventing enablement type. Will be nil if eventing is not enabled. |
| `connectorVersionInfraConfig` | `object` | This cofiguration provides infra configs like rate limit threshold which need to be configurable for every connector version |
| `configVariables` | `array` | Optional. Configuration for configuring the connection with an external system. |
| `status` | `object` | ConnectionStatus indicates the state of the connection. |
| `authConfig` | `object` | AuthConfig defines details of a authentication type. |
| `createTime` | `string` | Output only. Created time. |
| `connectionRevision` | `string` | Output only. Connection revision. This field is only updated when the connection is created or updated by User. |
| `labels` | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `connectorVersion` | `string` | Required. Connector version on which the connection is created. The format is: projects/*/locations/*/providers/*/connectors/*/versions/* Only global location is supported for ConnectorVersion resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_connections_list` | `SELECT` | `locationsId, projectsId` |
| `_projects_locations_connections_list` | `EXEC` | `locationsId, projectsId` |
