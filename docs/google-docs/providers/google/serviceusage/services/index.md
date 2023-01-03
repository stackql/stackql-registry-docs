---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - serviceusage
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.serviceusage.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the consumer and service. A valid name would be: - projects/123/services/serviceusage.googleapis.com |
| `parent` | `string` | The resource name of the consumer. A valid name would be: - projects/123 |
| `state` | `string` | Whether or not the service has been enabled for use by the consumer. |
| `config` | `object` | The configuration of the service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name` | Returns the service configuration and enabled state for a given service. |
| `batchEnable` | `EXEC` | `parent` | Enable multiple services on a project. The operation is atomic: if enabling any service fails, then the entire batch fails, and no state changes occur. To enable a single service, use the `EnableService` method instead. |
| `disable` | `EXEC` | `name` | Disable a service so that it can no longer be used with a project. This prevents unintended usage that may cause unexpected billing charges or security leaks. It is not valid to call the disable method on a service that is not currently enabled. Callers will receive a `FAILED_PRECONDITION` status if the target service is not currently enabled. |
