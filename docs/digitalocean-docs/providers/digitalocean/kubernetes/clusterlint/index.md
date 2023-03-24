---
title: clusterlint
hide_title: false
hide_table_of_contents: false
keywords:
  - clusterlint
  - kubernetes
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusterlint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.kubernetes.clusterlint</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `run_id` | `string` | Id of the clusterlint run that can be used later to fetch the diagnostics. |
| `completed_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the schedule clusterlint run request was completed. |
| `diagnostics` | `array` | An array of diagnostics reporting potential problems for the given cluster. |
| `requested_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the schedule clusterlint run request was made. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_clusterLintResults` | `SELECT` | `cluster_id` | To request clusterlint diagnostics for your cluster, send a GET request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/clusterlint`. If the `run_id` query<br />parameter is provided, then the diagnostics for the specific run is fetched.<br />By default, the latest results are shown.<br /><br />To find out how to address clusterlint feedback, please refer to<br />[the clusterlint check documentation](https://github.com/digitalocean/clusterlint/blob/master/checks.md).<br /> |
| `run_clusterLint` | `EXEC` | `cluster_id` | Clusterlint helps operators conform to Kubernetes best practices around<br />resources, security and reliability to avoid common problems while operating<br />or upgrading the clusters.<br /><br />To request a clusterlint run on your cluster, send a POST request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/clusterlint`. This will run all<br />checks present in the `doks` group by default, if a request body is not<br />specified. Optionally specify the below attributes.<br /><br />For information about the available checks, please refer to<br />[the clusterlint check documentation](https://github.com/digitalocean/clusterlint/blob/master/checks.md).<br /> |
