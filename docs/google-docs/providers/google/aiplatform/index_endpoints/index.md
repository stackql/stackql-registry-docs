---
title: index_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - index_endpoints
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>index_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.index_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the IndexEndpoint. |
| `description` | `string` | The description of the IndexEndpoint. |
| `deployedIndexes` | `array` | Output only. The indexes deployed in this endpoint. |
| `enablePrivateServiceConnect` | `boolean` | Optional. Deprecated: If true, expose the IndexEndpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set. |
| `labels` | `object` | The labels with user-defined metadata to organize your IndexEndpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| `network` | `string` | Optional. The full name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the IndexEndpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. network and private_service_connect_config are mutually exclusive. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/&#123;project&#125;/global/networks/&#123;network&#125;`. Where &#123;project&#125; is a project number, as in '12345', and &#123;network&#125; is network name. |
| `updateTime` | `string` | Output only. Timestamp when this IndexEndpoint was last updated. This timestamp is not updated when the endpoint's DeployedIndexes are updated, e.g. due to updates of the original Indexes they are the deployments of. |
| `createTime` | `string` | Output only. Timestamp when this IndexEndpoint was created. |
| `privateServiceConnectConfig` | `object` | Represents configuration for private service connect. |
| `etag` | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `publicEndpointEnabled` | `boolean` | Optional. If true, the deployed index will be accessible through public endpoint. |
| `displayName` | `string` | Required. The display name of the IndexEndpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| `publicEndpointDomainName` | `string` | Output only. If public_endpoint_enabled is true, this field will be populated with the domain name to use for this index endpoint. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `indexEndpointsId, locationsId, projectsId` | Gets an IndexEndpoint. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists IndexEndpoints in a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates an IndexEndpoint. |
| `delete` | `DELETE` | `indexEndpointsId, locationsId, projectsId` | Deletes an IndexEndpoint. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists IndexEndpoints in a Location. |
| `deploy_index` | `EXEC` | `indexEndpointsId, locationsId, projectsId` | Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it. Only non-empty Indexes can be deployed. |
| `find_neighbors` | `EXEC` | `indexEndpointsId, locationsId, projectsId` | Finds the nearest neighbors of each vector within the request. |
| `mutate_deployed_index` | `EXEC` | `indexEndpointsId, locationsId, projectsId` | Update an existing DeployedIndex under an IndexEndpoint. |
| `patch` | `EXEC` | `indexEndpointsId, locationsId, projectsId` | Updates an IndexEndpoint. |
| `read_index_datapoints` | `EXEC` | `indexEndpointsId, locationsId, projectsId` | Reads the datapoints/vectors of the given IDs. A maximum of 1000 datapoints can be retrieved in a batch. |
| `undeploy_index` | `EXEC` | `indexEndpointsId, locationsId, projectsId` | Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it's using. |
