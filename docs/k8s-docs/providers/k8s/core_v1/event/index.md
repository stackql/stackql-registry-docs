---
title: event
hide_title: false
hide_table_of_contents: false
keywords:
  - event
  - core_v1
  - k8s    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Kubernetes resources using SQL
custom_edit_url: null
image: /img/providers/k8s/stackql-k8s-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.event" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="action" /> | `string` | What action was taken/failed regarding to the Regarding object. |
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="count" /> | `integer` | The number of times this event has occurred. |
| <CopyableCode code="eventTime" /> | `string` | MicroTime is version of Time with microsecond level precision. |
| <CopyableCode code="firstTimestamp" /> | `string` | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. |
| <CopyableCode code="involvedObject" /> | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="lastTimestamp" /> | `string` | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. |
| <CopyableCode code="message" /> | `string` | A human-readable description of the status of this operation. |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="reason" /> | `string` | This should be a short, machine understandable string that gives the reason for the transition into the object's current status. |
| <CopyableCode code="related" /> | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |
| <CopyableCode code="reportingComponent" /> | `string` | Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. |
| <CopyableCode code="reportingInstance" /> | `string` | ID of the controller instance, e.g. `kubelet-xyzf`. |
| <CopyableCode code="series" /> | `object` | EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. |
| <CopyableCode code="source" /> | `object` | EventSource contains information for an event. |
| <CopyableCode code="type" /> | `string` | Type of this event (Normal, Warning), new types could be added in the future |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1EventForAllNamespaces" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind Event |
| <CopyableCode code="listCoreV1NamespacedEvent" /> | `SELECT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | list or watch objects of kind Event |
| <CopyableCode code="readCoreV1NamespacedEvent" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read the specified Event |
| <CopyableCode code="createCoreV1NamespacedEvent" /> | `INSERT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | create an Event |
| <CopyableCode code="deleteCoreV1CollectionNamespacedEvent" /> | `DELETE` | <CopyableCode code="namespace, cluster_addr, protocol" /> | delete collection of Event |
| <CopyableCode code="deleteCoreV1NamespacedEvent" /> | `DELETE` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | delete an Event |
| <CopyableCode code="patchCoreV1NamespacedEvent" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update the specified Event |
| <CopyableCode code="replaceCoreV1NamespacedEvent" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace the specified Event |
| <CopyableCode code="watchCoreV1EventListForAllNamespaces" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead. |
| <CopyableCode code="watchCoreV1NamespacedEvent" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | watch changes to an object of kind Event. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespacedEventList" /> | `EXEC` | <CopyableCode code="namespace, cluster_addr, protocol" /> | watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead. |
