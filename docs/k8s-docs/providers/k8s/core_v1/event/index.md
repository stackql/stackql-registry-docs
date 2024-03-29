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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.event</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `action` | `string` | What action was taken/failed regarding to the Regarding object. |
| `reason` | `string` | This should be a short, machine understandable string that gives the reason for the transition into the object's current status. |
| `reportingInstance` | `string` | ID of the controller instance, e.g. `kubelet-xyzf`. |
| `firstTimestamp` | `string` | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `related` | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `lastTimestamp` | `string` | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. |
| `type` | `string` | Type of this event (Normal, Warning), new types could be added in the future |
| `reportingComponent` | `string` | Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. |
| `involvedObject` | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |
| `eventTime` | `string` | MicroTime is version of Time with microsecond level precision. |
| `message` | `string` | A human-readable description of the status of this operation. |
| `series` | `object` | EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. |
| `count` | `integer` | The number of times this event has occurred. |
| `source` | `object` | EventSource contains information for an event. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1EventForAllNamespaces` | `SELECT` | `cluster_addr, protocol` | list or watch objects of kind Event |
| `listCoreV1NamespacedEvent` | `SELECT` | `namespace, cluster_addr, protocol` | list or watch objects of kind Event |
| `readCoreV1NamespacedEvent` | `SELECT` | `name, namespace, cluster_addr, protocol` | read the specified Event |
| `createCoreV1NamespacedEvent` | `INSERT` | `namespace, cluster_addr, protocol` | create an Event |
| `deleteCoreV1CollectionNamespacedEvent` | `DELETE` | `namespace, cluster_addr, protocol` | delete collection of Event |
| `deleteCoreV1NamespacedEvent` | `DELETE` | `name, namespace, cluster_addr, protocol` | delete an Event |
| `patchCoreV1NamespacedEvent` | `EXEC` | `name, namespace, cluster_addr, protocol` | partially update the specified Event |
| `replaceCoreV1NamespacedEvent` | `EXEC` | `name, namespace, cluster_addr, protocol` | replace the specified Event |
| `watchCoreV1EventListForAllNamespaces` | `EXEC` | `cluster_addr, protocol` | watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1NamespacedEvent` | `EXEC` | `name, namespace, cluster_addr, protocol` | watch changes to an object of kind Event. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedEventList` | `EXEC` | `namespace, cluster_addr, protocol` | watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead. |
