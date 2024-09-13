---
title: health_checks_aggregated
hide_title: false
hide_table_of_contents: false
keywords:
  - health_checks_aggregated
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

Creates, updates, deletes, gets or lists a <code>health_checks_aggregated</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_checks_aggregated</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.health_checks_aggregated" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="checkIntervalSec" /> | `integer` | How often (in seconds) to send a health check. The default value is 5 seconds. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in 3339 text format. |
| <CopyableCode code="grpcHealthCheck" /> | `object` |  |
| <CopyableCode code="healthyThreshold" /> | `integer` | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2. |
| <CopyableCode code="http2HealthCheck" /> | `object` |  |
| <CopyableCode code="httpHealthCheck" /> | `object` |  |
| <CopyableCode code="httpsHealthCheck" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` | Type of the resource. |
| <CopyableCode code="logConfig" /> | `object` | Configuration of logging on a health check. If logging is enabled, logs will be exported to Stackdriver. |
| <CopyableCode code="region" /> | `string` | [Output Only] Region where the health check resides. Not applicable to global health checks. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="sourceRegions" /> | `array` | The list of cloud regions from which health checks are performed. If any regions are specified, then exactly 3 regions should be specified. The region names must be valid names of Google Cloud regions. This can only be set for global health check. If this list is non-empty, then there are restrictions on what other health check fields are supported and what other resources can use this health check: - SSL, HTTP2, and GRPC protocols are not supported. - The TCP request field is not supported. - The proxyHeader field for HTTP, HTTPS, and TCP is not supported. - The checkIntervalSec field must be at least 30. - The health check cannot be used with BackendService nor with managed instance group auto-healing.  |
| <CopyableCode code="sslHealthCheck" /> | `object` |  |
| <CopyableCode code="tcpHealthCheck" /> | `object` |  |
| <CopyableCode code="timeoutSec" /> | `integer` | How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the healthCheck, either TCP, SSL, HTTP, HTTPS, HTTP2 or GRPC. Exactly one of the protocol-specific health check fields must be specified, which must match type field. |
| <CopyableCode code="unhealthyThreshold" /> | `integer` | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of all HealthCheck resources, regional and global, available to the specified project. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |

## `SELECT` examples

Retrieves the list of all HealthCheck resources, regional and global, available to the specified project. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
checkIntervalSec,
creationTimestamp,
grpcHealthCheck,
healthyThreshold,
http2HealthCheck,
httpHealthCheck,
httpsHealthCheck,
kind,
logConfig,
region,
selfLink,
sourceRegions,
sslHealthCheck,
tcpHealthCheck,
timeoutSec,
type,
unhealthyThreshold
FROM google.compute.health_checks_aggregated
WHERE project = '{{ project }}'; 
```
