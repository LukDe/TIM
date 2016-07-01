/**
 * This function generates an action creator. It receives the
 * type of the action, plus the name of the arguments to be in the
 * returned function.
 * An action retured by the action creator is a normal Redux action,
 * with the following format:
 * `{type: type, arg1: arg1, arg2: arg2, ...}`
 *
 * @param  {string}      type     Type of the action.
 * @param  {...[string]} argNames Name of the extra arguments.
 * @return {function}             Function that creates a Redux action.
 */
export function mkActionCreator (type, ...argNames) {
  return function (...args) {
    let action = { type }
    argNames.forEach((arg, index) => {
      action[argNames[index]] = args[index]
    })
    return action
  }
}
