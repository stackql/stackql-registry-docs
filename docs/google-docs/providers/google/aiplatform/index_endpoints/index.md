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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>index_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>index_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.index_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the IndexEndpoint. |
| <CopyableCode code="description" /> | `string` | The description of the IndexEndpoint. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this IndexEndpoint was created. |
| <CopyableCode code="deployedIndexes" /> | `array` | Output only. The indexes deployed in this endpoint. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the IndexEndpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="enablePrivateServiceConnect" /> | `boolean` | Optional. Deprecated: If true, expose the IndexEndpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your IndexEndpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="network" /> | `string` | Optional. The full name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the IndexEndpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. network and private_service_connect_config are mutually exclusive. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in '12345', and {network} is network name. |
| <CopyableCode code="privateServiceConnectConfig" /> | `object` | Represents configuration for private service connect. |
| <CopyableCode code="publicEndpointDomainName" /> | `string` | Output only. If public_endpoint_enabled is true, this field will be populated with the domain name to use for this index endpoint. |
| <CopyableCode code="publicEndpointEnabled" /> | `boolean` | Optional. If true, the deployed index will be accessible through public endpoint. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this IndexEndpoint was last updated. This timestamp is not updated when the endpoint's DeployedIndexes are updated, e.g. due to updates of the original Indexes they are the deployments of. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="indexEndpointsId, locationsId, projectsId" /> | Gets an IndexEndpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists IndexEndpoints in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an IndexEndpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="indexEndpointsId, locationsId, projectsId" /> | Deletes an IndexEndpoint. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="indexEndpointsId, locationsId, projectsId" /> | Updates an IndexEndpoint. |
| <CopyableCode code="deploy_index" /> | `EXEC` | <CopyableCode code="indexEndpointsId, locationsId, projectsId" /> | Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it. Only non-empty Indexes can be deployed. |
| <CopyableCode code="find_neighbors" /> | `EXEC` | <CopyableCode code="indexEndpointsId, locationsId, projectsId" /> | Finds the nearest neighbors of each vector within the request. |
| <CopyableCode code="mutate_deployed_index" /> | `EXEC` | <CopyableCode code="indexEndpointsId, locationsId, projectsId" /> | Update an existing DeployedIndex under an IndexEndpoint. |
| <CopyableCode code="read_index_datapoints" /> | `EXEC` | <CopyableCode code="indexEndpointsId, locationsId, projectsId" /> | Reads the datapoints/vectors of the given IDs. A maximum of 1000 datapoints can be retrieved in a batch. |
| <CopyableCode code="undeploy_index" /> | `EXEC` | <CopyableCode code="indexEndpointsId, locationsId, projectsId" /> | Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it's using. |

## `SELECT` examples

Lists IndexEndpoints in a Location.

```sql
SELECT
name,
description,
createTime,
deployedIndexes,
displayName,
enablePrivateServiceConnect,
encryptionSpec,
etag,
labels,
network,
privateServiceConnectConfig,
publicEndpointDomainName,
publicEndpointEnabled,
satisfiesPzi,
satisfiesPzs,
updateTime
FROM google.aiplatform.index_endpoints
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>index_endpoints</code> resource.

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
INSERT INTO google.aiplatform.index_endpoints (
locationsId,
projectsId,
encryptionSpec,
publicEndpointEnabled,
network,
privateServiceConnectConfig,
labels,
displayName,
description,
etag,
enablePrivateServiceConnect
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ encryptionSpec }}',
{{ publicEndpointEnabled }},
'{{ network }}',
'{{ privateServiceConnectConfig }}',
'{{ labels }}',
'{{ displayName }}',
'{{ description }}',
'{{ etag }}',
{{ enablePrivateServiceConnect }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: satisfiesPzi
      value: boolean
    - name: encryptionSpec
      value:
        - name: kmsKeyName
          value: string
    - name: publicEndpointEnabled
      value: boolean
    - name: updateTime
      value: string
    - name: createTime
      value: string
    - name: network
      value: string
    - name: privateServiceConnectConfig
      value:
        - name: serviceAttachment
          value: string
        - name: projectAllowlist
          value:
            - string
        - name: enablePrivateServiceConnect
          value: boolean
    - name: labels
      value: object
    - name: satisfiesPzs
      value: boolean
    - name: displayName
      value: string
    - name: description
      value: string
    - name: name
      value: string
    - name: publicEndpointDomainName
      value: string
    - name: etag
      value: string
    - name: deployedIndexes
      value:
        - - name: deploymentGroup
            value: string
          - name: privateEndpoints
            value:
              - name: matchGrpcAddress
                value: string
              - name: pscAutomatedEndpoints
                value:
                  - - name: projectId
                      value: string
                    - name: network
                      value: string
                    - name: matchAddress
                      value: string
              - name: serviceAttachment
                value: string
          - name: deployedIndexAuthConfig
            value:
              - name: authProvider
                value:
                  - name: audiences
                    value:
                      - string
                  - name: allowedIssuers
                    value:
                      - string
          - name: indexSyncTime
            value: string
          - name: enableAccessLogging
            value: boolean
          - name: dedicatedResources
            value:
              - name: machineSpec
                value:
                  - name: acceleratorCount
                    value: integer
                  - name: tpuTopology
                    value: string
                  - name: machineType
                    value: string
                  - name: acceleratorType
                    value: string
                  - name: reservationAffinity
                    value:
                      - name: reservationAffinityType
                        value: string
                      - name: values
                        value:
                          - string
                      - name: key
                        value: string
              - name: autoscalingMetricSpecs
                value:
                  - - name: target
                      value: integer
                    - name: metricName
                      value: string
              - name: maxReplicaCount
                value: integer
              - name: minReplicaCount
                value: integer
              - name: spot
                value: boolean
          - name: reservedIpRanges
            value:
              - string
          - name: displayName
            value: string
          - name: pscAutomationConfigs
            value:
              - - name: projectId
                  value: string
                - name: network
                  value: string
          - name: id
            value: string
          - name: index
            value: string
          - name: createTime
            value: string
          - name: automaticResources
            value:
              - name: minReplicaCount
                value: integer
              - name: maxReplicaCount
                value: integer
    - name: enablePrivateServiceConnect
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>index_endpoints</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.index_endpoints
SET 
encryptionSpec = '{{ encryptionSpec }}',
publicEndpointEnabled = true|false,
network = '{{ network }}',
privateServiceConnectConfig = '{{ privateServiceConnectConfig }}',
labels = '{{ labels }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
etag = '{{ etag }}',
enablePrivateServiceConnect = true|false
WHERE 
indexEndpointsId = '{{ indexEndpointsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>index_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.index_endpoints
WHERE indexEndpointsId = '{{ indexEndpointsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
