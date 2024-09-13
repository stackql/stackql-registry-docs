---
title: region_network_endpoint_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - region_network_endpoint_groups
  - compute
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

Creates, updates, deletes or gets an <code>region_network_endpoint_group</code> resource or lists <code>region_network_endpoint_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_network_endpoint_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_network_endpoint_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="annotations" /> | `object` | Metadata defined as annotations on the network endpoint group. |
| <CopyableCode code="appEngine" /> | `object` | Configuration for an App Engine network endpoint group (NEG). The service is optional, may be provided explicitly or in the URL mask. The version is optional and can only be provided explicitly or in the URL mask when service is present. Note: App Engine service must be in the same project and located in the same region as the Serverless NEG. |
| <CopyableCode code="cloudFunction" /> | `object` | Configuration for a Cloud Function network endpoint group (NEG). The function must be provided explicitly or in the URL mask. Note: Cloud Function must be in the same project and located in the same region as the Serverless NEG. |
| <CopyableCode code="cloudRun" /> | `object` | Configuration for a Cloud Run network endpoint group (NEG). The service must be provided explicitly or in the URL mask. The tag is optional, may be provided explicitly or in the URL mask. Note: Cloud Run service must be in the same project and located in the same region as the Serverless NEG. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="defaultPort" /> | `integer` | The default port used if the port number is not specified in the network endpoint. If the network endpoint type is either GCE_VM_IP, SERVERLESS or PRIVATE_SERVICE_CONNECT, this field must not be specified. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#networkEndpointGroup for network endpoint group. |
| <CopyableCode code="network" /> | `string` | The URL of the network to which all network endpoints in the NEG belong. Uses default project network if unspecified. |
| <CopyableCode code="networkEndpointType" /> | `string` | Type of network endpoints in this network endpoint group. Can be one of GCE_VM_IP, GCE_VM_IP_PORT, NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT, INTERNET_IP_PORT, SERVERLESS, PRIVATE_SERVICE_CONNECT, GCE_VM_IP_PORTMAP. |
| <CopyableCode code="pscData" /> | `object` | All data that is specifically relevant to only network endpoint groups of type PRIVATE_SERVICE_CONNECT. |
| <CopyableCode code="pscTargetService" /> | `string` | The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: asia-northeast3-cloudkms.googleapis.com |
| <CopyableCode code="region" /> | `string` | [Output Only] The URL of the region where the network endpoint group is located. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="size" /> | `integer` | [Output only] Number of network endpoints in the network endpoint group. |
| <CopyableCode code="subnetwork" /> | `string` | Optional URL of the subnetwork to which all network endpoints in the NEG belong. |
| <CopyableCode code="zone" /> | `string` | [Output Only] The URL of the zone where the network endpoint group is located. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkEndpointGroup, project, region" /> | Returns the specified network endpoint group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves the list of regional network endpoint groups available to the specified project in the given region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a network endpoint group in the specified project using the parameters that are included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkEndpointGroup, project, region" /> | Deletes the specified network endpoint group. Note that the NEG cannot be deleted if it is configured as a backend of a backend service. |
| <CopyableCode code="attach_network_endpoints" /> | `EXEC` | <CopyableCode code="networkEndpointGroup, project, region" /> | Attach a list of network endpoints to the specified network endpoint group. |
| <CopyableCode code="detach_network_endpoints" /> | `EXEC` | <CopyableCode code="networkEndpointGroup, project, region" /> | Detach the network endpoint from the specified network endpoint group. |

## `SELECT` examples

Retrieves the list of regional network endpoint groups available to the specified project in the given region.

```sql
SELECT
id,
name,
description,
annotations,
appEngine,
cloudFunction,
cloudRun,
creationTimestamp,
defaultPort,
kind,
network,
networkEndpointType,
pscData,
pscTargetService,
region,
selfLink,
size,
subnetwork,
zone
FROM google.compute.region_network_endpoint_groups
WHERE project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_network_endpoint_groups</code> resource.

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
INSERT INTO google.compute.region_network_endpoint_groups (
project,
region,
kind,
id,
creationTimestamp,
selfLink,
name,
description,
networkEndpointType,
size,
region,
zone,
network,
subnetwork,
defaultPort,
annotations,
cloudRun,
appEngine,
cloudFunction,
pscTargetService,
pscData
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ selfLink }}',
'{{ name }}',
'{{ description }}',
'{{ networkEndpointType }}',
'{{ size }}',
'{{ region }}',
'{{ zone }}',
'{{ network }}',
'{{ subnetwork }}',
'{{ defaultPort }}',
'{{ annotations }}',
'{{ cloudRun }}',
'{{ appEngine }}',
'{{ cloudFunction }}',
'{{ pscTargetService }}',
'{{ pscData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: networkEndpointType
        value: '{{ networkEndpointType }}'
      - name: size
        value: '{{ size }}'
      - name: region
        value: '{{ region }}'
      - name: zone
        value: '{{ zone }}'
      - name: network
        value: '{{ network }}'
      - name: subnetwork
        value: '{{ subnetwork }}'
      - name: defaultPort
        value: '{{ defaultPort }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: cloudRun
        value: '{{ cloudRun }}'
      - name: appEngine
        value: '{{ appEngine }}'
      - name: cloudFunction
        value: '{{ cloudFunction }}'
      - name: pscTargetService
        value: '{{ pscTargetService }}'
      - name: pscData
        value: '{{ pscData }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified region_network_endpoint_group resource.

```sql
DELETE FROM google.compute.region_network_endpoint_groups
WHERE networkEndpointGroup = '{{ networkEndpointGroup }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
