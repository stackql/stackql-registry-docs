---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - vpcaccess
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
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vpcaccess.connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name in the format `projects/*/locations/*/connectors/*`. |
| `ipCidrRange` | `string` | The range of internal addresses that follows RFC 4632 notation. Example: `10.132.0.0/28`. |
| `network` | `string` | Name of a VPC network. |
| `connectedProjects` | `array` | Output only. List of projects using the connector. |
| `machineType` | `string` | Machine type of VM Instance underlying connector. Default is e2-micro |
| `minInstances` | `integer` | Minimum value of instances in autoscaling group underlying the connector. |
| `minThroughput` | `integer` | Minimum throughput of the connector in Mbps. Default and min is 200. |
| `maxInstances` | `integer` | Maximum value of instances in autoscaling group underlying the connector. |
| `maxThroughput` | `integer` | Maximum throughput of the connector in Mbps. Default is 300, max is 1000. |
| `state` | `string` | Output only. State of the VPC access connector. |
| `subnet` | `object` | The subnet in which to house the connector |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectorsId, locationsId, projectsId` | Gets a Serverless VPC Access connector. Returns NOT_FOUND if the resource does not exist. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Serverless VPC Access connectors. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a Serverless VPC Access connector, returns an operation. |
| `delete` | `DELETE` | `connectorsId, locationsId, projectsId` | Deletes a Serverless VPC Access connector. Returns NOT_FOUND if the resource does not exist. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Serverless VPC Access connectors. |
| `patch` | `EXEC` | `connectorsId, locationsId, projectsId` | Updates a Serverless VPC Access connector, returns an operation. |
