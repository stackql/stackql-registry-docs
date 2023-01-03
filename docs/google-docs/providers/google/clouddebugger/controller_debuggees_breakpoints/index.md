---
title: controller_debuggees_breakpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - controller_debuggees_breakpoints
  - clouddebugger
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
<tr><td><b>Name</b></td><td><code>controller_debuggees_breakpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddebugger.controller_debuggees_breakpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Breakpoint identifier, unique in the scope of the debuggee. |
| `condition` | `string` | Condition that triggers the breakpoint. The condition is a compound boolean expression composed using expressions in a programming language at the source location. |
| `variableTable` | `array` | The `variable_table` exists to aid with computation, memory and network traffic optimization. It enables storing a variable once and reference it from multiple variables, including variables stored in the `variable_table` itself. For example, the same `this` object, which may appear at many levels of the stack, can have all of its data stored once in this table. The stack frame variables then would hold only a reference to it. The variable `var_table_index` field is an index into this repeated field. The stored objects are nameless and get their name from the referencing variable. The effective variable is a merge of the referencing variable and the referenced variable. |
| `location` | `object` | Represents a location in the source code. |
| `canaryExpireTime` | `string` | The deadline for the breakpoint to stay in CANARY_ACTIVE state. The value is meaningless when the breakpoint is not in CANARY_ACTIVE state. |
| `status` | `object` | Represents a contextual status message. The message can indicate an error or informational status, and refer to specific parts of the containing object. For example, the `Breakpoint.status` field can indicate an error referring to the `BREAKPOINT_SOURCE_LOCATION` with the message `Location not found`. |
| `action` | `string` | Action that the agent should perform when the code at the breakpoint location is hit. |
| `labels` | `object` | A set of custom breakpoint properties, populated by the agent, to be displayed to the user. |
| `userEmail` | `string` | E-mail address of the user that created this breakpoint |
| `evaluatedExpressions` | `array` | Values of evaluated expressions at breakpoint time. The evaluated expressions appear in exactly the same order they are listed in the `expressions` field. The `name` field holds the original expression text, the `value` or `members` field holds the result of the evaluated expression. If the expression cannot be evaluated, the `status` inside the `Variable` will indicate an error and contain the error text. |
| `state` | `string` | The current state of the breakpoint. |
| `expressions` | `array` | List of read-only expressions to evaluate at the breakpoint location. The expressions are composed using expressions in the programming language at the source location. If the breakpoint action is `LOG`, the evaluated expressions are included in log statements. |
| `logMessageFormat` | `string` | Only relevant when action is `LOG`. Defines the message to log when the breakpoint hits. The message may include parameter placeholders `$0`, `$1`, etc. These placeholders are replaced with the evaluated value of the appropriate expression. Expressions not referenced in `log_message_format` are not logged. Example: `Message received, id = $0, count = $1` with `expressions` = `[ message.id, message.count ]`. |
| `createTime` | `string` | Time this breakpoint was created by the server in seconds resolution. |
| `finalTime` | `string` | Time this breakpoint was finalized as seen by the server in seconds resolution. |
| `logLevel` | `string` | Indicates the severity of the log. Only relevant when action is `LOG`. |
| `stackFrames` | `array` | The stack at breakpoint time, where stack_frames[0] represents the most recently entered function. |
| `isFinalState` | `boolean` | When true, indicates that this is a final result and the breakpoint state will not change from here on. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `debuggeeId` | Returns the list of all active breakpoints for the debuggee. The breakpoint specification (`location`, `condition`, and `expressions` fields) is semantically immutable, although the field values may change. For example, an agent may update the location line number to reflect the actual line where the breakpoint was set, but this doesn't change the breakpoint semantics. This means that an agent does not need to check if a breakpoint has changed when it encounters the same breakpoint on a successive call. Moreover, an agent should remember the breakpoints that are completed until the controller removes them from the active list to avoid setting those breakpoints again. |
| `update` | `EXEC` | `debuggeeId, id` | Updates the breakpoint state or mutable fields. The entire Breakpoint message must be sent back to the controller service. Updates to active breakpoint fields are only allowed if the new value does not change the breakpoint specification. Updates to the `location`, `condition` and `expressions` fields should not alter the breakpoint semantics. These may only make changes such as canonicalizing a value or snapping the location to the correct line of code. |
